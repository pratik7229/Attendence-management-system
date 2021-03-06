from django.shortcuts import render, redirect
import requests
from .models import EmployeeInfo
from .models import DailyAttendenceInfor
from .models import sallery_Report
# Create your views here.


def homepage(request):
    return render(request, 'home.html')


def addempp(request):
    if request.method == "POST":
        name = request.POST.get('idname')
        email = request.POST.get('email')
        adharno = request.POST.get('adharno')
        photo = request.FILES.get('photo')
        phoneno = request.POST.get('phoneno')
        role = request.POST.get('role')
        sallery = request.POST.get('sallery')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        workexperience = request.POST.get('workexperience')
        recuritmentdate = request.POST.get('recuritmentdate')
        medicalhistory = request.POST.get('medicalhistory')
        employee = EmployeeInfo(name=name, email=email, adharno=adharno, photo=photo, phoneno=phoneno, role=role, sallery=sallery, dob=dob, education=education, workexperience=workexperience, recuritmentdate=recuritmentdate, medicalhistory=medicalhistory)
        employee.save()
        print('i am inside post')
        return redirect('home')
    else:
        print('i am inside get')
        return render(request, 'addemp.html')


def listemp(request):
    empl = EmployeeInfo.objects.all()
    return render(request, 'listemp.html', {'empl': empl})


def attendrep(request):
    if request.GET.get('Addatt'):
        return render(request,'sallery.html')
    print('i am inside attendrep')
    emplrep = DailyAttendenceInfor.objects.all()
    print(emplrep)
    return render(request, 'attend.html', {'emplrep': emplrep})


def salleryrep(request):
    sallery_report = sallery_Report.objects.all()
    return render(request, 'sallery.html',{'sallery_report': sallery_report})    # render request page name with html
