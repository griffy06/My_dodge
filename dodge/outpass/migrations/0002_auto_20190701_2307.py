
# Generated by Django 2.2.2 on 2019-07-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outpass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='permitted',
            field=models.CharField(default='no', max_length=100),
        ),
    ]