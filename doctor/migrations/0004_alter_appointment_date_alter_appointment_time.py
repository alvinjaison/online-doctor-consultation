# Generated by Django 4.0.6 on 2022-09-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_doctor_information_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
