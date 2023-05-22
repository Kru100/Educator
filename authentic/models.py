from djongo import models

class subject(models.Model):
    name = models.CharField(max_length=50)
    instructor_username = models.CharField(max_length=50)
    is_allowed = models.BooleanField(default=False)
    duration = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
class students(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=16)
    subject = models.ArrayField(model_container=subject, default=None)

class Instructor(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    qualification = models.TextField()
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=16)
    subject = models.ArrayField(model_container=subject, default=None)
    
class Admin(models.Model):
    password = models.CharField(max_length=16)

    