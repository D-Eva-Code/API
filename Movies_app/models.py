from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)  
    duration = models.FloatField()
    rating = models.FloatField() 
    typ = models.CharField(max_length=200, default ="Action")     
    
    def save(self, *args, **kwargs):
        if self.typ:
            self.typ = self.typ.capitalize()
        super().save(*args, **kwargs)                                                          
    
    def __str__(self):
        return self.name + str("-") + str( self.duration)
    