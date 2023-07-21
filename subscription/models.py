from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    subscription_id = models.CharField(max_length=255)
    country = CountryField(null=True)

    def __str__(self):
        print(self.country)
        return self.username.username


