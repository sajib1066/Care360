import uuid
from django.db import models
from django.utils.text import slugify

class TimesStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# Create your models here.
class Department(TimesStamp):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]  # সংক্ষিপ্ত UUID যোগ করা
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} , Status:{self.status}'
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        abstract = True
    
class State(TimesStamp):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]  # সংক্ষিপ্ত UUID যোগ করা
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        abstract = True

class Doctor(TimesStamp):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    
    MARITAL_CHOICES = (
        ('married', 'Married'),
        ('unmarrid', 'Unmarried'),
    )
    
    QUALIFICATION_CHOICES = [
        ('MD', 'Doctor of Medicine (MD)'),
        ('MBBS', 'Bachelor of Medicine, Bachelor of Surgery (MBBS)'),
        ('BDS', 'Bachelor of Dental Surgery (BDS)'),
        ('MS', 'Master of Surgery (MS)'),
        ('PHD', 'Doctor of Philosophy (PhD)'),
    ]
    # Designation Choices
    DESIGNATION_CHOICES = [
        ('SENIOR_DOCTOR', 'Senior Doctor'),
        ('JUNIOR_DOCTOR', 'Junior Doctor'),
        ('CONSULTANT', 'Consultant'),
        ('SPECIALIST', 'Specialist'),
        ('RESIDENT_DOCTOR', 'Resident Doctor'),
    ]

    # Blood Group Choices
    BLOOD_GROUP_CHOICES = [
        ('A_POSITIVE', 'A+'),
        ('B_POSITIVE', 'B+'),
        ('O_POSITIVE', 'O+'),
        ('AB_POSITIVE', 'AB+'),
        ('A_NEGATIVE', 'A-'),
        ('B_NEGATIVE', 'B-'),
        ('O_NEGATIVE', 'O-'),
        ('AB_NEGATIVE', 'AB-'),
    ]

    COUNTRY_CHOICES = [
        ('bangladesh', 'Bangladesh'),
        ('INDIA', 'India'),
        ('CHINA', 'China'),
    ]
    
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    marital_status = models.CharField(max_length=10, blank=True, null=True, choices=MARITAL_CHOICES)
    qualification = models.CharField(max_length=30, blank=True, null=True, choices=QUALIFICATION_CHOICES)
    designation = models.CharField(max_length=255, blank=True, null=True, choices=DESIGNATION_CHOICES)
    blood_group = models.CharField(max_length=10, blank=True, null=True, choices=BLOOD_GROUP_CHOICES)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True, choices=COUNTRY_CHOICES, default='bangladesh')
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]  # সংক্ষিপ্ত UUID যোগ করা
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name