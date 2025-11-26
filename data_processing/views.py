from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            #TODO: Add function to process data with SpaCy
            #TODO: Add redirect to upload form

    else:
        form = UploadFileForm()
    #TODO: return render for the upload template