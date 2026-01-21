from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

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
