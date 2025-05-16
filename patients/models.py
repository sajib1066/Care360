import uuid
from datetime import date
from django.db import models
from django.utils.text import slugify
from departments.models import Department, State
from datetime import date

# Create your models here
from doctors.models import TimesStamp


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


class Patient(TimesStamp):
    name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10, blank=True, null=True, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(uuid.uuid4())[:8]
        super().save(*args,
                     **kwargs)
        return self.slug

    def __str__(self):
        return self.name

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (
                    self.date_of_birth.month, self.date_of_birth.day)
            )
            return age
        return None
