# Generated by Django 5.0.6 on 2024-08-11 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0016_alter_dominogame_start_time_alter_player_coins_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 11, 20, 37, 25, 913397, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 11, 20, 37, 25, 913397, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 11, 20, 37, 25, 913397, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 11, 20, 37, 25, 913397, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='payPassValue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='payWinValue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='startAuto',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AddField(
            model_name='dominogame',
            name='sumAllPoints',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 20, 37, 25, 913397, tzinfo=datetime.timezone.utc)),
        ),
    ]
