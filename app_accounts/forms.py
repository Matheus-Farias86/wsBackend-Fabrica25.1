from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError("Este nome está em uso.")
        return username

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Senha Atual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nova Senha", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirme a Nova Senha", widget=forms.PasswordInput)
