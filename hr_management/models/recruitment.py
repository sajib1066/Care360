from django.db import models
from .employee import Position

class Recruitment(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('offered', 'Offered'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected')
    ]

    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='recruitments')
    candidate_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True)