# Generated by Django 3.0.6 on 2020-05-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0007_incident_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='plateNumber',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='postPlateCharacter',
            field=models.CharField(blank=True, default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='prePlateCharacters',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
