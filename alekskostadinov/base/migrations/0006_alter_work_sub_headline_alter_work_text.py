# Generated by Django 4.1.6 on 2023-02-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_work_body_work_favourite_work_sub_headline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='sub_headline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]