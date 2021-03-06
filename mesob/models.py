from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    ''' The booking model '''
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="booking", default=1)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    number_of_guests = models.IntegerField(null=False, blank=False)
    date_and_time = models.DateTimeField(auto_now=False, auto_now_add=False,
                                         default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
