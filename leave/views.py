from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from leave.forms import HomeForm
from .models import Post


class HomeView(TemplateView):

    template_name = 'leave/home.html'
    template_name2 = 'leave/home2.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            nameroll = name+roll
            form = HomeForm


        args = {'form': form, 'name': name, 'roll': roll, 'nameroll':nameroll}
        return render(request, self.template_name2, args)
