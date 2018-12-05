from django.urls import path
from .views import RoomBookView, adminapproveview, room_matrix


urlpatterns = [
    path('', RoomBookView.as_view(), name='roombook'),
    path('approve/', adminapproveview, name='approve'),
    path('home/', room_matrix, name='matrix'),
]
