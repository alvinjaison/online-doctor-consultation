# Generated by Django 4.0.6 on 2022-09-12 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_prescription_relation_with_meal_perscription_test_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perscription_medicine',
            old_name='days',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='perscription_medicine',
            old_name='time',
            new_name='frequency',
        ),
        migrations.RenameField(
            model_name='perscription_medicine',
            old_name='medicine_description',
            new_name='instruction',
        ),
    ]
