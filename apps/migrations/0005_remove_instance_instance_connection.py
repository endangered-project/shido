# Generated by Django 5.0.1 on 2024-01-16 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_apply_limitation_blank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instanceinstancerelation',
            name='instance_instance_connection',
        ),
        migrations.RemoveField(
            model_name='instanceinstancerelation',
            name='instance_object_1',
        ),
        migrations.RemoveField(
            model_name='instanceinstancerelation',
            name='instance_object_2',
        ),
        migrations.DeleteModel(
            name='InstanceInstanceConnection',
        ),
        migrations.DeleteModel(
            name='InstanceInstanceRelation',
        ),
    ]
