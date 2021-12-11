from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request, 'qr_app/home.html')

@login_required(login_url='/qr/login')
def attendance(request):
    if request.method == "GET":
        form = AttendanceForm()
        return render(request, 'qr_app/attendance.html', {'form': form})
    else:
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/qr/list/')

@login_required(login_url='/qr/login')
def attendance_list(request):
    queryset = Attendance.objects.all()
    return render(request, 'qr_app/attendance_list.html', {'queryset': queryset})

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')