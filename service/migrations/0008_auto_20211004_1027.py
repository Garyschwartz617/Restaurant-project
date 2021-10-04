# Generated by Django 3.2.7 on 2021-10-04 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_course'),
        ('service', '0007_auto_20211004_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.course'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
