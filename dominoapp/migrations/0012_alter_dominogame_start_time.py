# Generated by Django 5.0.6 on 2024-08-09 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0011_player_coins_alter_dominogame_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 12, 35, 3, 356584, tzinfo=datetime.timezone.utc)),
        ),
    ]
