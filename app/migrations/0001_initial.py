# Generated by Django 2.2 on 2019-04-19 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateTimeField(default=django.utils.timezone.now)),
                ('smile', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='1')),
                ('coment', models.CharField(max_length=100)),
                ('zaryadka', models.BooleanField(default=True)),
            ],
        ),
    ]