from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField()
    message=models.TextField()
    created=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   
    def __str__(self):
        return self.user.get_full_name() 