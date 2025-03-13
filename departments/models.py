import uuid
from datetime import date
from django.db import models
from django.utils.text import slugify


# Choices
GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
MARITAL_CHOICES = [('married', 'Married'), ('unmarried', 'Unmarried')]
QUALIFICATION_CHOICES = [('MD', 'Doctor of Medicine (MD)'),
                         ('MBBS', 'Bachelor of Medicine, Bachelor of Surgery (MBBS)'),
                         ('BDS', 'Bachelor of Dental Surgery (BDS)'),
                         ('MS', 'Master of Surgery (MS)'),
                         ('PHD', 'Doctor of Philosophy (PhD)')]

DESIGNATION_CHOICES = [('SENIOR_DOCTOR', 'Senior Doctor'),
                       ('JUNIOR_DOCTOR', 'Junior Doctor'),
                       ('CONSULTANT', 'Consultant'),
                       ('SPECIALIST', 'Specialist'),
                       ('RESIDENT_DOCTOR', 'Resident Doctor')]

BLOOD_GROUP_CHOICES = [('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'),
                       ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')]

COUNTRY_CHOICES = [('bangladesh', 'Bangladesh'),
                   ('india', 'India'), ('china', 'China')]


class TimesStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(TimesStamp):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} , Status:{self.status}'

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['-created_at']

