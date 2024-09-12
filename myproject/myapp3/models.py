from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    signal_processed = models.BooleanField(default=False)
