# Generated by Django 3.0.6 on 2020-05-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=65)),
                ('facility_email', models.EmailField(max_length=254, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('facilty_location', models.CharField(max_length=100)),
                ('lon', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('lat', models.FloatField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
            ],
            options={
                'verbose_name_plural': 'Medical Facilities',
            },
        ),
    ]
