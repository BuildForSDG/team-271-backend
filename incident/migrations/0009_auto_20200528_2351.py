# Generated by Django 3.0.6 on 2020-05-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0008_auto_20200528_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='plateNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='postPlateCharacter',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='prePlateCharacters',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
