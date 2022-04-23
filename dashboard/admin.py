from django.contrib import admin
from .models import EmployeeInfo
from .models import DailyAttendenceInfor
from .models import sallery_Report
# Register your models here.
admin.site.register(EmployeeInfo)
admin.site.register(DailyAttendenceInfor)
admin.site.register(sallery_Report)
