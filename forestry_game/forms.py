from django import forms

class RegisterForm(forms.Form):
  username = forms.CharField(required=True, min_length=3, max_length=15)
  password = forms.CharField(required=True, min_length=6, max_length=50)
  email = forms.EmailField(required=True)
