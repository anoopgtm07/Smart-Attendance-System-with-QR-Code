from django.urls import path
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('', views.attendance, name="add_attendance"),
    path('list/', views.attendance_list),
    path('register/', UserRegisterView.as_view(), name = 'register'),
]