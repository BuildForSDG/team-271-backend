# Generated by Django 3.0.6 on 2020-05-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0002_auto_20200520_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='postPlateCharacter',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='prePlateCharacters',
        ),
        migrations.AddField(
            model_name='incident',
            name='fatalities',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='plateNumber',
            field=models.CharField(max_length=20),
        ),
    ]
