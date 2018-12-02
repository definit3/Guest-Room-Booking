from django.urls import path
from .views import RoomBookView


urlpatterns = [
    path('', RoomBookView.as_view()),
]
