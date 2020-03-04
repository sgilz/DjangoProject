from django.db import models

# Create your models here.
import uuid

class Hygrometer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.IntegerField(verbose_name='Humedad')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)