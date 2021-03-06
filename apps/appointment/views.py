from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Appointments, Status

def index(request):

    return render(request, 'appointment/index.html')

def create(request):
    if not User.userManager.registration(request):
        return redirect ('/dashboard')
    else:
        return redirect ('/')

def login(request):
    if not User.userManager.login(request):
        return redirect ('/dashboard')
    else:
        return redirect ('/')

def dashboard(request):
    user = User.userManager.get(id=request.session['id'])
    my_appointments = Appointments.appointmentsManager.all()
    data = {
        'user': user,
        'my_appointments': my_appointments,
    }
    return render(request, 'appointment/dashboard.html', data)

def create_appointment(request, user_id):
    user = User.userManager.get(id=request.session['id'])
    my_appointments = Appointments.appointmentsManager.all()
    data = {
        'user': user,
        'my_appointments': my_appointments,
    }
    if not Appointments.appointmentsManager.create_appointment(request):
        return redirect('/processappointment', data)
    else:
        return redirect(request, '/dashboard')
def processappointment(request):
    user = User.userManager.get(id=request.session['id'])
    my_appointments = Appointments.appointmentsManager.all()
    data = {
        'user': user,
        'my_appointments': my_appointments,
    }
    return render(request, 'appointment/dashboard.html')
def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request,user_id):
    Appointments.appointmentsManager.get(id=user_id).delete()
    return redirect('/dashboard')
def edit(request, user_id):
        return render(request, 'appointment/edit.html')
