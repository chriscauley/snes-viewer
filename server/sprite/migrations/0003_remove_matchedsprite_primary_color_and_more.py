# Generated by Django 4.0.5 on 2022-06-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprite', '0002_plmsprite_match_xy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchedsprite',
            name='primary_color',
        ),
        migrations.RemoveField(
            model_name='plmsprite',
            name='primary_color',
        ),
        migrations.AddField(
            model_name='matchedsprite',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='plmsprite',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='matchedsprite',
            name='color',
            field=models.CharField(blank=True, choices=[('black', 'black'), ('blue', 'blue'), ('dust', 'dust'), ('eye', 'eye'), ('gold', 'gold'), ('gray', 'gray'), ('green', 'green'), ('mixed', 'mixed'), ('orange', 'orange'), ('pink', 'pink'), ('purple', 'purple'), ('red', 'red'), ('white', 'white')], max_length=16, null=True),
        ),
    ]
