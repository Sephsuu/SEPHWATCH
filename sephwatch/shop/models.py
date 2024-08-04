from django.db import models

# Create your models here.
class Watch(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    release_date = models.DateField()
    image = models.ImageField(upload_to='watches/', default="default.png")

    def __str__(self):
        return f"{self.brand} - {self.model}"