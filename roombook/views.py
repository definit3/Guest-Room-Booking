from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BookForm, AdminApprove
from .models import Room
from django.http import HttpResponse
import datetime


def room_matrix(request):
    rooms = Room.objects.all()
    no_of_rooms = len(rooms)
    return render(request, 'roombook/roommatrix.html', {'rooms': rooms, 'no_of_rooms': no_of_rooms, })


class RoomBookView(TemplateView):

    template_name = 'roombook/home.html'
    template_name2 = 'roombook/home2.html'

    def get(self, request):

        room = Room.objects.filter(vacant=False)
        for i in room:
            if i.vacant_date < datetime.date.today():
                i.vacant = True
                i.save()
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            x = form.cleaned_data['no_of_rooms']
            room = Room.objects.filter(vacant=True)[:x]
            if len(room) >= x:
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                delta = end_date - start_date
                delta = delta.days * 200
                args = {'form': form, 'days': delta}
                return render(request, self.template_name2, args)

            else:
                return HttpResponse('Enough rooms not available')


def adminapproveview(request):
    templateadmin = 'roombook/adminapprove.html'
    templateadmin2 = 'roombook/adminapprove2.html'

    if request.method == "POST":

        form = AdminApprove(request.POST)

        if form.is_valid():
            book = form.cleaned_data.get('choice')
            x = book.no_of_rooms
            room = Room.objects.filter(vacant=True)[:x]
            y = form.cleaned_data['like']

            if len(room) >= x and y:
                book.status = 'Approved'
                book.approve = True
                book.save()
                for i in room:
                    i.vacant = False
                    i.vacant_date = book.end_date
                    i.save()
                args = {'form': form, 'room': room, }
                return render(request, templateadmin2, args)
            else:
                book.status = 'Declined'
                book.save()
                return HttpResponse('Declined')

    else:
        form = AdminApprove()
        return render(request, templateadmin, {'form': form})
