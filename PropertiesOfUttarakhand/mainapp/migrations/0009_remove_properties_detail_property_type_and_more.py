# Generated by Django 4.0.1 on 2022-11-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_properties_detail_commercial_property_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties_detail',
            name='property_type',
        ),
        migrations.AddField(
            model_name='properties_detail',
            name='commercial_property_type',
            field=models.CharField(blank=True, choices=[('officespace', 'Office Space'), ('foodcourt', 'Food Court'), ('shoppingcomplex', 'Shopping Complex'), ('retailshops', 'Retail Shops'), ('plots', 'Plots'), ('hotel', 'Hotel')], max_length=255),
        ),
        migrations.AddField(
            model_name='properties_detail',
            name='resdential_property_type',
            field=models.CharField(blank=True, choices=[('stdio', 'Studio'), ('1bhk', '1 BHK'), ('2bhk', '2 BHK'), ('3bhk', '3 BHK'), ('house', 'House'), ('villa', 'Villa'), ('plots', 'Plots')], max_length=255),
        ),
    ]
