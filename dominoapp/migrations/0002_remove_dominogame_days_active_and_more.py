# Generated by Django 5.1.3 on 2024-12-26 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dominogame',
            name='days_active',
        ),
        migrations.AddField(
            model_name='dominogame',
            name='hours_active',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284980, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284878, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284899, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284913, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284926, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 26, 15, 52, 17, 284700, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastTimeInSystem',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 26, 15, 52, 17, 283994, tzinfo=datetime.timezone.utc)),
        ),
    ]