from django.db import models

# Create your models here.
import uuid

class Hygrometer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, null=True)
    value = models.IntegerField(verbose_name='Humedad')
    latitude = models.FloatField(verbose_name='Latitud', default=0)
    length = models.FloatField(verbose_name='Longitud', default=0)
    ground = models.CharField(max_length=30, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)