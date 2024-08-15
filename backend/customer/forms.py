from django import forms
from django.db import models
from .models import Contact,Customer
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Contact
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-4','placeholder':'Your email'}),
            'subject':forms.TextInput(attrs={'class':'form-control mb-4','placeholder':'Your subject'}),
            'message':forms.Textarea(attrs={'class':'form-control mb-4','placeholder':'Your message'}),
            
        }
        
        
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'})),
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'})),
    last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'})),
    email=forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'})),
    password=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'})),
    password2=forms.CharField(max_length=100, label='password again', widget=forms.EmailInput(attrs={'class':'form-control'})),
    
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        password2=cleaned_data.get('password2')
        if password and password2 !=password2:
            raise forms.ValidationError('sifreler eyni deyil')
        
    def clean_email(self):
        email=self.cleaned._data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('BU email movcuddur')
        return email
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu username artiq movcuddur')
        return username
    
    def save(self):
        cleaned_data=self.cleaned_data
        username=cleaned_data.get('username')
        first