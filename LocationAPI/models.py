from django.db import models

# Create your models here.
class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.CharField(max_length=120, blank=True, null=True)
    longitude = models.CharField(max_length=120, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'location'
