# Generated by Django 4.0.3 on 2022-04-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_bookings_room_alter_bookings_venue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='Time',
            new_name='Starttime',
        ),
        migrations.AddField(
            model_name='bookings',
            name='endtime',
            field=models.IntegerField(default=0),
        ),
    ]