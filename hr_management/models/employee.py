from django.db import models
from django.contrib.auth import get_user_model
from departments.models import Department

User = get_user_model()

class Position(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.department}"

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    emergency_contact = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"