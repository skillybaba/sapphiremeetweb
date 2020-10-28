from django.db import models

# Create your models here.

class user(models.Model):
    id=models.AutoField
    name = models.TextField(max_length=300)
    email=models.TextField(max_length=300)
    passcode= models.TextField(max_length=300)
    def __str__(self):
        return str(id)

