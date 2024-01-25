from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customers(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    username = models.CharField(max_length=200,default="",unique=True)
    address = models.TextField()
    phone = models.IntegerField()
    user = models.OneToOneField(User,related_name='customer',on_delete=models.CASCADE)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

