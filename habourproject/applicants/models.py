from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    is_applicant = models.BooleanField(default = False, blank = False)
    is_recruiter = models.BooleanField(default = False, blank = False)
    
