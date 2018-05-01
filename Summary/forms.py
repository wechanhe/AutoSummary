from django import forms

class UploadFileForm(forms.Form):
    upload_user = forms.CharField(max_length=20,required=False)
    type = forms.CharField(max_length=20,required=False)
    file = forms.FileField()