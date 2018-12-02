from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BookForm


class RoomBookView(TemplateView):

    template_name = 'leave/home.html'
    template_name2 = 'leave/home2.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            form = BookForm
        args = {'form': form, 'name': name, }
        return render(request, self.template_name2, args)
