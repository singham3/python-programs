# Generated by Django 2.0.7 on 2018-08-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='image_url',
            field=models.ImageField(default='static/imag/AB-3.jpg', upload_to='media/imag'),
        ),
    ]
