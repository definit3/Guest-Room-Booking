from django import forms
from . models import Post
from django.contrib.admin.widgets import AdminDateWidget


class HomeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Full Name'
        }
    ))
    roll = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Roll Number'
        }
    ))
    leave_start_date = forms.DateField(widget = forms.SelectDateWidget())
    leave_end_date = forms.DateField(widget = forms.SelectDateWidget())
    reason = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the reason for leave'
        }
    ))

    class Meta:
        model = Post
        fields = ('name', 'roll', 'leave_start_date', 'leave_end_date', 'reason')