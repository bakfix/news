from django import forms
from .models import Comment
class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8, required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
