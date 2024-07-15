from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder':'Логин'
            }
        ),
        required = False,
        validators=[RegexValidator(r'[^0-9а-яА-ЯёЁ]', "Введите логин латиницой")],
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder':'Ваша почта'
            }
        ),
        required = False
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder':'Введите пароль'
            }
        ),
        required = False
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder':'Повторите пароль'
            }
        ),
        required = False
    )
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length= 254,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин'
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Пароль'
            }
        ),
        required=False
    )
    
    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно"
        )
    }
    
    
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Введите пароль', code="invalid")
        return password
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Такого пользователя не существует', cjde='invalid')
        return username
