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


class AdminApprove(forms.Form):
    choice = forms.ModelChoiceField(queryset=Book.objects.all().filter(approve=False),
                                    widget=forms.Select(attrs={'class': 'regDropDown'}))
    # accept = forms.RadioSelect()
    # decline = forms.RadioSelect()
    CHOICES = [(True, 'Accept'),
               (False, 'Decline')]

    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

