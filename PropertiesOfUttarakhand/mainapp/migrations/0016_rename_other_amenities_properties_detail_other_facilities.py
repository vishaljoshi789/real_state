# Generated by Django 4.0.1 on 2022-12-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_rename_dimensions_properties_detail_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties_detail',
            old_name='other_amenities',
            new_name='other_facilities',
        ),
    ]