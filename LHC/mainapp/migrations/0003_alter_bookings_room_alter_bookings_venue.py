# Generated by Django 4.0.3 on 2022-04-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_bookings_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='Room',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Venue',
            field=models.CharField(default='NULL', max_length=3),
        ),
    ]
