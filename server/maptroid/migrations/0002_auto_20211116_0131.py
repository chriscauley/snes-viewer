# Generated by Django 3.2.7 on 2021-11-16 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maptroid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('youtube', 'youtube')], default='youtube', max_length=16)),
                ('external_id', models.CharField(max_length=24)),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(upload_to='channel_icons')),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='channel_name',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='external_id',
            field=models.CharField(default=1, max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='source',
            field=models.CharField(choices=[('youtube', 'youtube')], default='youtube', max_length=16),
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maptroid.channel'),
            preserve_default=False,
        ),
    ]