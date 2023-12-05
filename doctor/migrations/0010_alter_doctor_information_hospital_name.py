# Generated by Django 4.0.6 on 2022-09-09 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('doctor', '0009_prescription_extra_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_information',
            name='hospital_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital_information'),
        ),
    ]
