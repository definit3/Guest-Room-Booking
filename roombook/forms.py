from django import forms
from . models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Full Name'
        }
    ))
    no_of_rooms = forms.IntegerField()
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    reason = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Reason for booking'
        }
    ))

    class Meta:
        model = Book
        fields = ('name', 'no_of_rooms', 'start_date', 'end_date', 'reason')
