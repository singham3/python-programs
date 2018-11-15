from django.db import models

class demoBank(models.Model):
    name=models.CharField(max_length=50)
    value=models.DecimalField(max_digits=10, decimal_places=2)
    material=models.CharField(max_length=20)
    locations=models.CharField(max_length=100)
    image_url=models.CharField(max_length=400)

    def __str__(self):
        return self.name