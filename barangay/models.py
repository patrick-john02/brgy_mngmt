from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('resident', 'Resident'),  
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} - {self.user_type}"

class Resident(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
 
    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),
        ('separated', 'Separated'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    household_number = models.CharField(max_length=50, blank=True, null=True)
    head_of_family = models.BooleanField(default=False)
    voter_status = models.BooleanField(default=False)
    id_number = models.CharField(max_length=20, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address}"
