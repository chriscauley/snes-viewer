# Generated by Django 3.2.7 on 2022-03-01 20:49

from django.db import migrations, models
import maptroid.models


class Migration(migrations.Migration):

    dependencies = [
        ('maptroid', '0019_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='smilesprite',
            name='template',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='run',
            name='data',
            field=models.JSONField(blank=True, default=maptroid.models.default_run_data),
        ),
        migrations.AlterField(
            model_name='smilesprite',
            name='category',
            field=models.CharField(blank=True, choices=[('block', 'block'), ('geo', 'geo'), ('hex', 'hex'), ('item', 'item'), ('enemy', 'enemy'), ('obstacle', 'obstacle'), ('door', 'door'), ('station', 'station'), ('animation', 'animation'), ('trash', 'trash')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='smilesprite',
            name='color',
            field=models.CharField(blank=True, choices=[('black', 'black'), ('blue', 'blue'), ('eye', 'eye'), ('gold', 'gold'), ('gray', 'gray'), ('green', 'green'), ('orange', 'orange'), ('pink', 'pink'), ('purple', 'purple'), ('red', 'red'), ('white', 'white')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='smilesprite',
            name='modifier',
            field=models.CharField(blank=True, choices=[('composite', 'composite'), ('inblock', 'inblock'), ('inegg', 'inegg'), ('repspawn', 'repspawn')], max_length=16, null=True),
        ),
    ]
