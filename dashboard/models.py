from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
    # personal information
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    photo = models.ImageField(null=True, blank= True, upload_to='pics')
    adharno = models.BigIntegerField(blank=False, unique=True)
    phoneno = models.BigIntegerField(blank=False, unique=True)
    role = models.TextField(blank=False, null=False)
    sallery = models.FloatField(blank=False)
    dob = models.DateField(blank=False, null=False)
    education = models.TextField(blank=True)
    workexperience = models.IntegerField(blank=False)
    recuritmentdate = models.DateField(blank=False, null=False)
    medicalhistory = models.TextField(blank=True)


class DailyAttendenceInfor(models.Model):
    emp_id = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    intime = models.TimeField()
    outtime = models.TimeField()
    remark = models.CharField(max_length=2,null=True)
    '''
    #daily Attendence Information
    #adharno no Foreign key
    #presentdays = models.IntegerField()
    #absentdays = models.IntegerField()
    #overtimehrs = models.TimeField()

    sallery report attendence information
    adhar number foreign key'''
    
class sallery_Report(models.Model):
    emp_id = models.ForeignKey(EmployeeInfo,on_delete=models.CASCADE)
    present_days = models.IntegerField()
    Absent_days = models.IntegerField()
    Working_days = models.IntegerField()
    rate = models.IntegerField(null=False)
    salary = models.FloatField()
    overtimr_hrs = models.FloatField()
    overtime_salary = models.FloatField()
    total_sallery = models.FloatField()
    advance_sallery = models.FloatField()
    balance_sallary = models.FloatField()
    date_of_payment = models.DateField()
    payment_mode = models.CharField(max_length= 10)



    ''' # Sallery Infromation
    adharno foreign key
    rate = models.FloatField()
    totalpayment = models.FloatField()
    advancesallery = models.FloatField()
    netTotal = models.FloatField()
    paymentmode = models.TextField()
    sallery = models.FloatField()'''




