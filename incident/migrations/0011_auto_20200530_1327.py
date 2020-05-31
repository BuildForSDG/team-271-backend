# Generated by Django 3.0.6 on 2020-05-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0010_auto_20200528_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
