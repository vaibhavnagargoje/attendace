from django.contrib import admin
from .models import Staff,Attendance,ExamDetail

# Register your models here.
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(ExamDetail)