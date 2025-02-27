from django import forms
from .models import Item
from .models import Profile
from django.contrib.auth.models import User


class ItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.FileField()

    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'contact_info']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        

        fields = ['image']

