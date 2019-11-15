from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=100)
    roaster = models.CharField(max_length=100, blank =True)
    brew_method = models.CharField(max_length=100, blank = True)
    taste_note = models.CharField(max_length=500, blank = True)
    rating = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)