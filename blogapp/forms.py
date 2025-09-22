from django import forms
from .models import profilepicture,postitem

class ProfileForm(forms.ModelForm):
    class Meta:
        model=profilepicture
        fields=['username','profile_pic']

class PostForm(forms.ModelForm):
    class Meta:
        model=postitem
        fields='__all__'

