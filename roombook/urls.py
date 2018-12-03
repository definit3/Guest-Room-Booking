from django.urls import path
from .views import RoomBookView, adminapproveview, room_matrix


urlpatterns = [
    path('', RoomBookView.as_view()),
    path('approve/', adminapproveview),
    path('home/', room_matrix),
]
