from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Expense(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)


