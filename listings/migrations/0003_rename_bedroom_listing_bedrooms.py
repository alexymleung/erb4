# Generated by Django 4.2.17 on 2024-12-23 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_bedrooms_listing_bathrooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bedroom',
            new_name='bedrooms',
        ),
    ]