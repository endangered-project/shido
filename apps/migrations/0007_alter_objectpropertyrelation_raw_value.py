# Generated by Django 5.0.1 on 2024-02-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_propertytype_raw_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpropertyrelation',
            name='raw_value',
            field=models.CharField(max_length=1000000),
        ),
    ]
