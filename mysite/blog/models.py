from  django.db import models

class bloginfo(models.Model):
    name=models.CharField(max_length=50)
    value=models.DecimalField(max_digits=10, decimal_places=2)
    material=models.CharField(max_length=20)
    location=models.CharField(max_length=1000)
    image_url=models.FileField(upload_to='imag/')

    def __str__(self):
        return self.name



class product(models.Model):
    name=models.CharField(max_length=100)
    textbox=models.CharField(max_length=1000)
    image_product=models.FileField(upload_to='imagepro/')


    def __str__(self):
        return self.name


class card(models.Model):
    textarea=models.CharField(max_length=1000)


