from django.db import models
from datetime import datetime



class Advisor(models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    advisor_email = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
