# Generated by Django 3.0.8 on 2020-08-09 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealStateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=32)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=32)),
                ('expenses_price', models.DecimalField(decimal_places=2, max_digits=32)),
                ('square_meters', models.DecimalField(decimal_places=2, max_digits=32)),
                ('town', models.CharField(max_length=256)),
                ('raw_data', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]