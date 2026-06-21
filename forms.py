from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

class RegistrationForm(UserCreationForm):
#     pass
# class RegistrationForm(forms.Form):
    recaptcha=ReCaptchaField()
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)