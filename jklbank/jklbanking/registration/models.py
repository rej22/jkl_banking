from django.db import models

class Personal_data(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

