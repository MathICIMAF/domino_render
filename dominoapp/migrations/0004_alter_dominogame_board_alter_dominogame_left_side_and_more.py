# Generated by Django 5.0.6 on 2024-06-08 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0003_player_tiles_dominogame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='board',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='left_side',
            field=models.SmallIntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='maxScore',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='next_player',
            field=models.SmallIntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='right_side',
            field=models.SmallIntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 8, 18, 40, 6, 888434, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='variant',
            field=models.CharField(choices=[('d6', 'Double 6'), ('d9', 'Double 9')], max_length=10),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='winner',
            field=models.SmallIntegerField(default=-1, null=True),
        ),
    ]
