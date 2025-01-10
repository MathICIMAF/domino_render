# Generated by Django 5.1.3 on 2024-12-26 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0002_remove_dominogame_days_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691630, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691529, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691548, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691562, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='lastTime4',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691575, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='password',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 26, 16, 22, 50, 691351, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastTimeInSystem',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 26, 16, 22, 50, 690573, tzinfo=datetime.timezone.utc)),
        ),
    ]