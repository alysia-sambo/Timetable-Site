from django.db import models

TRANSPORT_TYPES = [
    ("BUS", "Bus"),
    ("FERRY", "Ferry"),
    ("TRAIN", "Train"),
]
    
class TransportStop(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    transport_type = models.CharField(choices=TRANSPORT_TYPES, default="BUS")
    
    def __str__(self):
        return self.code

