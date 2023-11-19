from django import forms
from .models import Images # Replace YourModelName with the actual name of your model

class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = Images  # Replace YourModelName with the actual name of your model
        fields = ['image']  # Add other fields if needed