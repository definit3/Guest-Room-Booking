from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BookForm, AdminApprove
from .models import Room, Book


class RoomBookView(TemplateView):

    template_name = 'roombook/home.html'
    template_name2 = 'roombook/home2.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # x = form.cleaned_data['no_of_rooms']
            # room = Room.objects.filter(vacant=True)[:x]
            # for i in room:
            #     i.vacant = False
            #     i.save()
            room = Room.objects.all()
        args = {'form': form, 'room': room, }
        return render(request, self.template_name2, args)


def adminapproveview(request):
    templateadmin = 'roombook/adminapprove.html'
    templateadmin2 = 'roombook/adminapprove2.html'

    if request.method == "POST":

        form = AdminApprove(request.POST)

        if form.is_valid():
            book = form.cleaned_data.get('choice')
            book.approve = True
            book.save()
            x = book.no_of_rooms
            room = Room.objects.filter(vacant=True)[:x]
            for i in room:
                i.vacant = False
                i.save()

        args = {'form': form, 'room': room, }
        return render(request, templateadmin2, args)

    else:
        form = AdminApprove()
        return render(request, templateadmin, {'form': form})
