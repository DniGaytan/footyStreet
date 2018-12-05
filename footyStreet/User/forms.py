from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
        	'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'usuario'}),
        	'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'correo'}),
}
