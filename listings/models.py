from django.db import models
from datetime import datetime

from advisors.models import Advisor


class Listing (models.Model):
    advisor= models.ForeignKey(Advisor, on_delete=models.CASCADE, related_name='listings')
    title= models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    daysrequired = models.IntegerField()
    suggested_season= models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Photo_2= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published=models.BooleanField(default=True)
    list_date= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title