from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm as BaseAuthenticationForm,
)
from .models import Statement, User

class RegisterForm(UserCreationForm):
    username = forms.CharField( label='Введите ваш логин',widget=forms.TextInput(attrs={'class':'form-control', 'pattern':'\w+'}))
    FIO = forms.CharField( label='Введите ваше ФИО',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField ( label='Введите Пароль',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField ( label='Подтверждение Пароля',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone=forms.CharField ( label='Номер телефона в формате +7(XXX)-XXX-XX-XX',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField ( label='Почта',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "FIO",
            "phone",
            "email",
        ]
        


class AuthenticationForm(BaseAuthenticationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CreateStatementForm(forms.ModelForm):
    number=forms.CharField( label="Государственный регистрационный номер" ,widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField( label='Описание', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Statement
        fields = [
            "number",
            "description",
            "date_time",

        ]
        widgets = {
            "description": forms.Textarea(),
            "date_time": forms.DateTimeInput({"type": "datetime-local"}),
        }

class StatementStatusForm(forms.ModelForm):
    forms.DateTimeField

    class Meta:
        model = Statement
        fields = ["status"]