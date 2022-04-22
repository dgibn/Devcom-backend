# Generated by Django 4.0.3 on 2022-04-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(default='John Doe', max_length=200)),
                ('Venue', models.CharField(choices=[('Complex A', 'A'), ('Complex B', 'B'), ('Complex C', 'C')], default='NULL', max_length=13)),
                ('Room', models.CharField(default='NULL', max_length=6)),
                ('Date', models.CharField(default='01-01-0001', max_length=10)),
                ('Time', models.IntegerField(default=0)),
            ],
        ),
    ]