# Generated by Django 2.1.1 on 2018-09-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0005_auto_20180920_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Our_Customers_1', models.FileField(upload_to='about/')),
            ],
        ),
    ]
