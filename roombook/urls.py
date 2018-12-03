from django.urls import path
from .views import RoomBookView, adminapproveview


urlpatterns = [
    path('', RoomBookView.as_view()),
    path('approve/', adminapproveview),
]
