from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from .employee import Employee

User = get_user_model()

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    review_date = models.DateField()
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()
    goals = models.TextField()