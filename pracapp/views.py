from django.shortcuts import render
from django.shortcuts import render, redirect  
# Create your views here.
from .models import User
from .forms import DoctorForm,PatientForm
from email import message
from django.contrib import messages
from django.contrib.auth import login

def home(request):
    return render(request,"home.html") 

# Create your views for doctor.  
def doctor_view(request):  
    if request.method == "POST":  
        form = DoctorForm(request.POST)  
        if form.is_valid():  
          user = form.save(commit=False)
          user.save()
          login(request, user)
             
    else:  
        form = DoctorForm()  
    return render(request,'create_view_doctor.html',{'form':form})  

def Patient_view(request):  
    if request.method == "POST":  
        form = PatientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = PatientForm()  
    return render(request,'create_view_patient.html',{'form':form})  

def show_doctor(request):  
    DPs = User.objects.all()  
   
    context = {
    'DPs':DPs,
   
  }
    return render(request,"show_doctor.html",context)  