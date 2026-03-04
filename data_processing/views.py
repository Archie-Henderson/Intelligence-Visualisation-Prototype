import io
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import IntelligenceReport, Entity, EntityIntelligenceReport, AccessLog, EntityProfile
from pypdf import PdfReader
from .spacy_event_pipeline import extract_and_store_spacy_for_report
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest
from django.utils import timezone

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'web_page/index.html', context=context_dict)

def upload(request):
    if request.method != "POST":
        return render(request, "web_page/upload.html")

    if not request.FILES.get("file"):
        return render(request, "web_page/upload.html", {"error": "Please choose a file."})

    f = request.FILES["file"]
    filename = (f.name or "").lower()
    raw = f.read()

    # save original file
    f.seek(0)
    fs = FileSystemStorage()
    fs.save(f.name, f)

    # extract text properly
    if filename.endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(raw))
            text = "\n".join((page.extract_text() or "") for page in reader.pages).strip()
        except Exception as e:
            return render(request, "web_page/upload.html", {"error": f"Could not read PDF: {e}"})

        if not text:
            return render(request, "web_page/upload.html", {
                "error": "Couldn’t extract text from this PDF (it may be scanned). Please upload a text-based PDF or a .txt file."
            })
    else:
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", errors="replace")

        if not text.strip():
            return render(request, "web_page/upload.html", {"error": "File looks empty."})

    # create report
    report = IntelligenceReport.objects.create(
        fullReport=text,
        isAiGenerated=True,
        isApproved=False,
        createdBy=request.user if request.user.is_authenticated else None,
    )

    # run spaCy and store extracted entities/links
    extract_and_store_spacy_for_report(report.reportID)

    return redirect(reverse("data_processing:workspace", args=[report.reportID]))
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'web_page/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect(reverse('data_processing:index'))
        
    return render(request, 'web_page/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('data_processing:index'))

def _log_action(user, report, action_type: str):
    """
    action_type must be one of: 'view', 'add', 'edit', 'delete'
    """
    AccessLog.objects.create(
        user=user,
        report=report,
        actionType=action_type,
    )

def _clean_str(value: str) -> str:
    return (value or "").strip()

def _parse_int_or_none(value: str):
    value = _clean_str(value)
    if value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return "INVALID"

#report page
@login_required
def report_detail(request, report_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)

    # show only active links and active entities
    links = (
        EntityIntelligenceReport.objects
        .select_related("entity")
        .filter(report=report, isDeleted=False, entity__isDeleted=False)
        .order_by("entity__name")
    )

    _log_action(request.user, report, "view")

    return render(request, "web_page/report_detail.html", {
        "report": report,
        "links": links,
    })

# A) Edit entity name/type
@login_required
@require_POST
def edit_entity(request, entity_id: int):
    entity = get_object_or_404(Entity, entityID=entity_id, isDeleted=False)

    name = _clean_str(request.POST.get("name"))
    entity_type = _clean_str(request.POST.get("type"))

    if not name:
        return HttpResponseBadRequest("Entity name cannot be empty.")

    valid_types = {t for (t, _) in Entity.ENTITY_TYPES}
    if entity_type not in valid_types:
        return HttpResponseBadRequest("Invalid entity type.")

    # update
    entity.name = name
    entity.type = entity_type
    entity.source = "USER"  # mark that a user edited it
    entity.save(update_fields=["name", "type", "source", "updatedAt"])

    # If you pass ?next=/some/url we redirect there, else go back
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:index")
    return redirect(next_url)

# Unlink entity from report
@login_required
@require_POST
def unlink_entity_from_report(request, report_id: int, entity_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)
    link = get_object_or_404(
        EntityIntelligenceReport,
        report=report,
        entity__entityID=entity_id,
        isDeleted=False
    )

    link.isDeleted = True
    link.source = "USER"
    link.save(update_fields=["isDeleted", "source", "updatedAt"])

    _log_action(request.user, report, "delete")  # unlink behaves like delete in audit terms

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:report_detail", args=[report_id])
    return redirect(next_url)

# Relink entity to report
@login_required
@require_POST
def relink_entity_to_report(request, report_id: int, entity_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)
    link = get_object_or_404(
        EntityIntelligenceReport,
        report=report,
        entity__entityID=entity_id,
        isDeleted=True
    )

    link.isDeleted = False
    link.source = "USER"
    link.save(update_fields=["isDeleted", "source", "updatedAt"])

    _log_action(request.user, report, "add")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:report_detail", args=[report_id])
    return redirect(next_url)

#Add missing entity (create + link)
@login_required
@require_POST
def add_entity_to_report(request, report_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)

    name = _clean_str(request.POST.get("name"))
    entity_type = _clean_str(request.POST.get("type"))

    if not name:
        return HttpResponseBadRequest("Entity name cannot be empty.")

    valid_types = {t for (t, _) in Entity.ENTITY_TYPES}
    if entity_type not in valid_types:
        return HttpResponseBadRequest("Invalid entity type.")

    entity = Entity.objects.create(
        name=name,
        type=entity_type,
        source="USER",
    )

    EntityIntelligenceReport.objects.create(
        entity=entity,
        report=report,
        isDeleted=False,
        source="USER",
    )

    _log_action(request.user, report, "add")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:report_detail", args=[report_id])
    return redirect(next_url)

# Delete wrong ones 
@login_required
@require_POST
def soft_delete_entity(request, entity_id: int):
    entity = get_object_or_404(Entity, entityID=entity_id, isDeleted=False)

    entity.isDeleted = True
    entity.source = "USER"
    entity.save(update_fields=["isDeleted", "source", "updatedAt"])

    # also unlink it from all reports
    EntityIntelligenceReport.objects.filter(entity=entity, isDeleted=False).update(isDeleted=True, source="USER")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:index")
    return redirect(next_url)

# Edit “profile block” fields
@login_required
@require_POST
def edit_entity_profile(request, entity_id: int):
    entity = get_object_or_404(Entity, entityID=entity_id, isDeleted=False)

    # create profile if missing
    profile, _created = EntityProfile.objects.get_or_create(entity=entity)

    age_val = _parse_int_or_none(request.POST.get("age"))
    if age_val == "INVALID":
        return HttpResponseBadRequest("Age must be an integer.")

    address = _clean_str(request.POST.get("address"))
    role = _clean_str(request.POST.get("role"))
    notes = _clean_str(request.POST.get("notes"))

    profile.age = age_val
    profile.address = address or None
    profile.role = role or None
    profile.notes = notes or None
    profile.source = "USER"
    profile.save()

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("data_processing:index")
    return redirect(next_url)

@login_required
def workspace(request, report_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)

    links = (
        EntityIntelligenceReport.objects
        .select_related("entity")
        .filter(report=report, isDeleted=False, entity__isDeleted=False)
        .order_by("entity__type", "entity__name")
    )

    return render(request, "web_page/workspace.html", {
        "report": report,
        "links": links,
    })

@login_required
@require_POST
def approve_report(request, report_id: int):
    report = get_object_or_404(IntelligenceReport, reportID=report_id)

    report.isApproved = True
    report.approvedAt = timezone.now()
    report.approvedBy = request.user
    report.save(update_fields=["isApproved", "approvedAt", "approvedBy"])

    _log_action(request.user, report, "edit")
    return redirect(reverse("data_processing:workspace", args=[report.reportID]))