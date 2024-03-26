from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )  
    
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)  #for authentication purposes
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    password = models.CharField(max_length= 100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True, choices=ROLE_CHOICES)
         
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table='customer'

