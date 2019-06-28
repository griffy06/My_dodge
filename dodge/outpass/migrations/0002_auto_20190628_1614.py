# Generated by Django 2.2.2 on 2019-06-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outpass', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='destination',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='vehicle',
            field=models.CharField(default=None, max_length=100),
        ),
    ]