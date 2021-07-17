from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='places/',
        null=True, 
        blank=True )
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '-' + self.country
    
    class Meta:
        ordering = ['visited']
