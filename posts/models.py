from django.db import models

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField()
    agreement = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    client = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
    carModel = models.CharField(max_length=50, null=True)
    carNumber = models.CharField(max_length=50, null=True)
    carNumber_masked = models.CharField(max_length=50, null=True)
    birth = models.CharField(max_length=50, null=True)
    trim = models.CharField(max_length=50, null=True)
    fuel = models.CharField(max_length=50, null=True)
    driveType = models.CharField(max_length=50, null=True)
    airbag = models.CharField(max_length=50, null=True)
    mileage = models.CharField(max_length=50, null=True)
    eventDate = models.CharField(max_length=50, null=True)
    repairCost = models.CharField(max_length=50, null=True)
    proposedCompensation = models.CharField(max_length=50, null=True)
    insuranceCompany = models.CharField(max_length=50, null=True)
    insuranceCompany_me = models.CharField(max_length=50, null=True)
    faultRatio = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    others1 = models.CharField(max_length=50, null=True)
    others2 = models.CharField(max_length=50, null=True)
    others3 = models.CharField(max_length=50, null=True)
    note = models.CharField(max_length=500, null=True)
    addition = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)
    opinion = models.CharField(max_length=500, null=True)
    image1 = models.FileField(upload_to='posts', null=True)
    image2 = models.FileField(upload_to='posts', null=True)
    image3 = models.FileField(upload_to='posts', null=True)
    image4 = models.FileField(upload_to='posts', null=True)
    image5 = models.FileField(upload_to='posts', null=True)
    image6 = models.FileField(upload_to='posts', null=True)
    image7 = models.FileField(upload_to='posts', null=True)
    image8 = models.FileField(upload_to='posts', null=True)
    image9 = models.FileField(upload_to='posts', null=True)
    image10 = models.FileField(upload_to='posts', null=True)
    image11 = models.FileField(upload_to='posts', null=True)
    image12 = models.FileField(upload_to='posts', null=True)
    image13 = models.FileField(upload_to='posts', null=True)
    image14 = models.FileField(upload_to='posts', null=True)
    image15 = models.FileField(upload_to='posts', null=True)
    image16 = models.FileField(upload_to='posts', null=True)
    image17 = models.FileField(upload_to='posts', null=True)
    file_name = models.CharField(max_length=50, null=True)
   