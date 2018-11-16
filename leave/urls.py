from django.contrib import admin
from django.urls import path,include
from leave.views import HomeView

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomeView.as_view()),
]