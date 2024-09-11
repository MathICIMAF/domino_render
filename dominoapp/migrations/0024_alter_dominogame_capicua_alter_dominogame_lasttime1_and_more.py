# Generated by Django 5.0.6 on 2024-09-11 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0023_alter_dominogame_lasttime1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='capicua',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 11, 15, 37, 55, 184871, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 11, 15, 37, 55, 184871, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 11, 15, 37, 55, 184871, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 11, 15, 37, 55, 185809, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='maxScore',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='next_player',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='payPassValue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='payWinValue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 15, 37, 55, 183815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='starter',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='winner',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
