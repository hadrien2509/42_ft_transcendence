# Generated by Django 5.0 on 2024-05-28 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='player1_id',
            new_name='p1_id',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='player1_name',
            new_name='p1_name',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='player1_score',
            new_name='p1_score',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='player2_id',
            new_name='p2_id',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='player2_name',
            new_name='p2_name',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='player2_score',
            new_name='p2_score',
        ),
    ]
