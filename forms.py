from django import forms
from .models import Item, Profile
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description'})
    )
    image = forms.FileField()
    

    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'contact_info']
        # Add a placeholder for the contact_info field
        widgets = {
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact info'})
        }
        

class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

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