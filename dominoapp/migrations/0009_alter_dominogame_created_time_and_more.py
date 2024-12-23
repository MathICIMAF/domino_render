# Generated by Django 5.1.3 on 2024-12-23 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0008_alter_dominogame_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109935, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='hours_active',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109861, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109875, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109885, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109894, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109727, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastTimeInSystem',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 20, 52, 12, 109206, tzinfo=datetime.timezone.utc)),
        ),
    ]
