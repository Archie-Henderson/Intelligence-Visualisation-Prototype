from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    def clean_file(self):
        uploaded_file = self.cleaned_data['file']

        # Check MIME type (text/plain)
        if uploaded_file.content_type != 'text/plain':
            raise forms.ValidationError("Only .txt files are allowed.")

        # Optional: check extension
        if not uploaded_file.name.endswith('.txt'):
            raise forms.ValidationError("File must have a .txt extension.")

        return uploaded_file