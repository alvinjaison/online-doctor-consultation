# Generated by Django 4.0.6 on 2022-09-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_rename_perscription_medicine_prescription_medicine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_information',
            name='login_status',
            field=models.CharField(blank=True, default='offline', max_length=200, null=True),
        ),
    ]
