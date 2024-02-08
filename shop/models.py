# models.py
from django.db import models
import datetime
import os

def getFilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)

class Cagagory(models.Model):  # Keeping the intentional typo
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFilename, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    Cagagory = models.ForeignKey(Cagagory, on_delete=models.CASCADE)  # Keeping the intentional typo
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    Product_image = models.ImageField(upload_to=getFilename, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
