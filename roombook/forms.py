from django import forms
from . models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Full Name'
        }
    ))

    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    no_of_rooms = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter No of Rooms'
        }
    ))

    class Meta:
        model = Book
        fields = ('name', 'tart_date', 'end_date', 'no_of_rooms')
