from django import forms


class UploadImageForm(forms.Form):
    image = forms.ImageField(
        label='Select an image',
        widget=forms.FileInput(attrs={'class': 'upload-field'})
    )
