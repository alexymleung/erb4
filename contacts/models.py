from django.db import models
from datetime import datetime
from listings.views import Listing

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.ForeignKey(Listing,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.TextField(blank = True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    
    def __str__(self):
        return self.name
