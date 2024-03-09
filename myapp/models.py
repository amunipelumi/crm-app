from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=128)

    province = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.first_name}  {self.last_name}'
