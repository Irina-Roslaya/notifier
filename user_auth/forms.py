from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['email'].required = True
        self.fields['first_name'].label = 'Имя'
        self.fields['first_name'].required = True
        self.fields['last_name'].label = 'Фамилия'
        self.fields['last_name'].required = True
        self.fields['username'].label = 'Никнейм'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повторите пароль'
