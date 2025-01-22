# Generated by Django 5.1.3 on 2025-01-22 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0007_remove_player_user_player_email_player_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34832, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34747, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34759, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34773, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34783, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34612, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastTimeInSystem',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 21, 0, 31, 34072, tzinfo=datetime.timezone.utc)),
        ),
    ]
