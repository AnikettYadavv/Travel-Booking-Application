# Generated by Django 5.1.7 on 2025-03-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveloption',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
