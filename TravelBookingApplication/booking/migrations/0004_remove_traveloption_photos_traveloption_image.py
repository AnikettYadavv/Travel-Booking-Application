# Generated by Django 5.1.7 on 2025-03-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_rename_available_seats_traveloption_available_seats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveloption',
            name='photos',
        ),
        migrations.AddField(
            model_name='traveloption',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='travel_images/'),
        ),
    ]
