# Generated by Django 3.2.7 on 2021-09-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_alter_measurement_amount_per_kilo'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='measurement',
            field=models.ManyToManyField(blank=True, to='kitchen.Combo'),
        ),
    ]
