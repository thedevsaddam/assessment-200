# Generated by Django 3.2 on 2022-06-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='cows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='farmers',
            name='goats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='farmers',
            name='initial_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='farmers',
            name='sheeps',
            field=models.IntegerField(default=0),
        ),
    ]
