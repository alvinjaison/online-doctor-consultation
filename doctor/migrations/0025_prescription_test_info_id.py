# Generated by Django 4.0.6 on 2022-09-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0024_merge_20220914_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='test_info_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
