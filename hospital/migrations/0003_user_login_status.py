# Generated by Django 4.0.6 on 2022-09-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patient_login_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_status',
            field=models.CharField(blank=True, default='offline', max_length=200, null=True),
        ),
    ]
