from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm): # Usamos o UserCreationForm do Django como base e adicionamos o campo email
    email = forms.EmailField(required=True, label='Email') # Adiciona o campo email como obrigatório

    class Meta:
        model = User # Utilizamos o model User do próprio Django que vem com autenticação
        fields = ['username', 'email', 'password1', 'password2'] # Os campos que serão exibidos no formulário

    def clean_email(self): # Verifica se o email está em uso
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

class ChangePasswordForm(PasswordChangeForm): # Utilizamos o PasswordChangeForm do Django para facilitar a alteração de senha
    old_password = forms.CharField(label="Senha Atual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nova Senha", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirme a Nova Senha", widget=forms.PasswordInput)
