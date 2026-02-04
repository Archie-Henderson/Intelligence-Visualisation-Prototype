from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserForm
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    context_dict = {}
    return render(request, 'index.html', context=context_dict)

def upload(request):

    if request.method == "POST" and request.FILES.get("file"):
        f = request.FILES["file"]

        fs = FileSystemStorage()
        fs.save(f.name, f)

    return render(request, 'upload.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('index')
        
    return render(request, 'login.html')