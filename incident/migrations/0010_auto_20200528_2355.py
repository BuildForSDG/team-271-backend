# Generated by Django 3.0.6 on 2020-05-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0009_auto_20200528_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='plateNumber',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='incident',
            name='prePlateCharacters',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]