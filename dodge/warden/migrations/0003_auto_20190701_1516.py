# Generated by Django 2.2.2 on 2019-07-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warden', '0002_auto_20190701_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
