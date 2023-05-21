from djongo import models

class students(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=16)
    
    