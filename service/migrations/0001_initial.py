# Generated by Django 3.2.7 on 2021-09-05 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('kitchen', '0002_alter_measurement_amount_per_kilo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('O', 'Open'), ('P', 'Pending'), ('C', 'Closed')], default='O', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('order_number', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
                ('measurement', models.ManyToManyField(to='kitchen.Combo')),
            ],
        ),
        migrations.CreateModel(
            name='Singular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.dish')),
            ],
        ),
    ]