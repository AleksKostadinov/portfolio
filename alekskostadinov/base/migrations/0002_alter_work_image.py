# Generated by Django 4.1.6 on 2023-02-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
