from django.db import models

# Create your models here.
class AllClothes(models.Model):
    item_Name = models.CharField(max_length=10)
    item_location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.item_Name