# Generated by Django 3.2.20 on 2023-09-05 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0003_alter_agesverification_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 5, 10, 8, 5, 718139)),
        ),
    ]
