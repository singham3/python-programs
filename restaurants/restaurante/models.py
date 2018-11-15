from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=50)
    slider_image = models.FileField(upload_to='slider/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name= models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Post_Title(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    Post_Title_image = models.FileField(upload_to='post title/')

    def __str__(self):
        return self.name

class Post_Detail(models.Model):
    name = models.CharField(max_length=50)
    textbox = models.TextField(max_length=5000)


class About_Page(models.Model):
    name = models.CharField(max_length=50)
    text_line = models.TextField(max_length=500)
    mail_id = models.CharField(max_length=100)
    about_image = models.FileField(upload_to='about/')

    def __str__(self):
        return self.name

class Commenter_Name(models.Model):
    name = models.CharField(max_length=50)
    contain = models.CharField(max_length=250)
    Our_Customers_image = models.FileField(upload_to='about/')

    def __str__(self):
        return self.name

class Our_Customers(models.Model):
    Our_Customers_1 = models.FileField(upload_to='about/')


class Send_Message(models.Model):
    Full_Name = models.CharField(max_length=100)
    Phone_Number = models.DecimalField(max_digits=13, decimal_places = 2)
    Email_Address =models.CharField(max_length=100)
    Message = models.TextField(max_length=5000)

