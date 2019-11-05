from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control', "placeholder": "Username", "id": "form_username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control', "placeholder": "Password", "id": "form_password"}))