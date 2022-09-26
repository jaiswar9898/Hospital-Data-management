from sqlite3 import Row
from django import forms

from django.forms import CharField, Form, PasswordInput
from django.forms import ModelForm
from .models import User

class DoctorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','profile_picture','address','password','ConfirmPassword')


    def clean_email(self):
       email = self.cleaned_data.get('email')
       qs = User.objects.filter(email=email)
       if qs.exists():
          raise forms.ValidationError("email is taken")
       return email

    def clean(self):

       cleaned_data = super().clean()
       password = cleaned_data.get("password")
       ConfirmPassword = cleaned_data.get("ConfirmPassword")

       if password != ConfirmPassword:
          self.add_error("ConfirmPassword", "Your passwords must match")
       return cleaned_data
    def save(self, commit=True):
  # Save the provided password in hashed format
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password"])
       user.set_password(self.cleaned_data["ConfirmPassword"])
       if commit:
          user.save()
       return user

class PatientForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','profile_picture','address','password','ConfirmPassword')


    def clean_email(self):
       email = self.cleaned_data.get('email')
       qs = User.objects.filter(email=email)
       if qs.exists():
          raise forms.ValidationError("email is taken")
       return email

    def clean(self):

       cleaned_data = super().clean()
       password = cleaned_data.get("password")
       ConfirmPassword = cleaned_data.get("ConfirmPassword")

       if password != ConfirmPassword:
          self.add_error("ConfirmPassword", "Your passwords must match")
       return cleaned_data
    def save(self, commit=True):
  # Save the provided password in hashed format
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password"])
       user.set_password(self.cleaned_data["ConfirmPassword"])
       if commit:
          user.save()
       return user
  
