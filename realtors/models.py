from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank = True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    foto_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    foto_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.name