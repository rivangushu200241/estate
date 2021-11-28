# Generated by Django 3.2.4 on 2021-07-27 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0002_auto_20210702_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='property_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]