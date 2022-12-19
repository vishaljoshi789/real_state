# Generated by Django 4.0.1 on 2022-12-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_properties_detail_out_property_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties_detail',
            name='bathroom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='properties_detail',
            name='bedroom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='properties_detail',
            name='kitchen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]