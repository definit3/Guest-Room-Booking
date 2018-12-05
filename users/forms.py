from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Student, Warden
from django import forms


class UserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'same as your roll no.',
        }


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'type': 'text', 'id': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'type': 'password', 'id': 'password'}))


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_name',
            'father_name',
            'enrollment_no',
            ]
