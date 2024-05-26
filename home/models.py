from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15,null=True)
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    file = models.FileField(upload_to='uploads/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)    

