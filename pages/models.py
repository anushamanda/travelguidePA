from django.db import models
from listings.models import Listing


class Pages(models.Model):
    listing=models.ForeignKey(Listing, on_delete=models.CASCADE)
