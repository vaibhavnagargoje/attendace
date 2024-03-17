from django.db import models
from django.utils import timezone
from django.db.models import Count

# Create your models here.

class Staff(models.Model):
    class Department_Choices(models.TextChoices):

        MATH='Mathematics'
        CS='Computer Science'
        PHY='Physics'
    
    Sr_no = models.IntegerField(unique=True)
    Staff_Name= models.CharField(max_length=100)
    
    Experiance = models.IntegerField()
    Department = models.CharField(max_length=30, choices =Department_Choices.choices,default="")
    Extra_Info= models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.Staff_Name
    

class Attendance(models.Model):
    
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,to_field='Sr_no')
    date = models.DateField(default=timezone.now, editable=False)
    morning_present = models.BooleanField(default=False)
    afternoon_present = models.BooleanField(default=False)

    class Meta:
            # Add any constraints or options here if needed
        pass

    @property
    def total_attendance_month(self):
        return Attendance.objects.filter(staff=self.staff, date__month=self.date.month, morning_present=True).count()

    @property
    def total_attendance_week(self):
        current_week = timezone.now().isocalendar()[1]
        return Attendance.objects.filter(staff=self.staff, date__week=current_week, morning_present=True).count()

    def __str__(self):
        return f"{self.staff.Staff_Name} - {self.date}"
    


class ExamDetail(models.Model):
    ExamName= models.CharField(max_length=100)
    Date_time=models.DateTimeField(blank=True, null=True)
    Duration = models.DurationField("duration",blank=True,null=True)
    Information= models.TextField()

    def __str__(self):
        return self.ExamName