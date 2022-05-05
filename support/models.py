
# Create your models here. 
from django.db import models

class Info(models.Model):
    title_text = models.CharField(max_length=50)
    content_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')