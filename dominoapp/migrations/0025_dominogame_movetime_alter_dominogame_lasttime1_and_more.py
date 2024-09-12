# Generated by Django 5.0.6 on 2024-09-12 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0024_alter_dominogame_capicua_alter_dominogame_lasttime1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominogame',
            name='moveTime',
            field=models.SmallIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 12, 19, 39, 49, 825791, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 12, 19, 39, 49, 826787, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 12, 19, 39, 49, 826787, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 12, 19, 39, 49, 826787, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 12, 19, 39, 49, 825791, tzinfo=datetime.timezone.utc)),
        ),
    ]
