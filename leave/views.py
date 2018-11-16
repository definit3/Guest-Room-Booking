from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from leave.forms import HomeForm
from .models import Post


class HomeView(TemplateView):

    template_name = 'leave/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()

            text = form.cleaned_data['name']
            form = HomeForm

        # text = form.cleaned_data['name']

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
