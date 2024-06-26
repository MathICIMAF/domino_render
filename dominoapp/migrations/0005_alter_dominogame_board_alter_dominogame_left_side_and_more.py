# Generated by Django 5.0.6 on 2024-06-26 15:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominoapp', '0004_alter_dominogame_board_alter_dominogame_left_side_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominogame',
            name='board',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='left_side',
            field=models.SmallIntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='maxScore',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='next_player',
            field=models.SmallIntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='player1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='dominoapp.player'),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='player2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='dominoapp.player'),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='player3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to='dominoapp.player'),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='player4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4', to='dominoapp.player'),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='right_side',
            field=models.SmallIntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='scoreTeam2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 15, 46, 33, 597643, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='status',
            field=models.CharField(choices=[('wt', 'waiting_players'), ('ru', 'running'), ('ready', 'ready_to_play')], default='wt', max_length=32),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='variant',
            field=models.CharField(choices=[('d6', 'Double 6'), ('d9', 'Double 9')], default='d6', max_length=10),
        ),
        migrations.AlterField(
            model_name='dominogame',
            name='winner',
            field=models.SmallIntegerField(blank=True, default=-1, null=True),
        ),
    ]
