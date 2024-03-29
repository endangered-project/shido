# Generated by Django 5.0 on 2023-12-24 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initialize_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='class_instance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instanceinstanceconnection',
            name='first_instance_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first_instance_class', to='apps.class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instanceinstanceconnection',
            name='second_instance_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='second_instance_class', to='apps.class'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClassInstanceRelation',
        ),
    ]
