# Generated by Django 2.2.4 on 2019-08-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simulation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='simulation',
            name='start_time',
            field=models.CharField(max_length=100),
        ),
    ]
