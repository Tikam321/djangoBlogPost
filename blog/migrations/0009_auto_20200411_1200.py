# Generated by Django 2.2.4 on 2020-04-11 06:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200410_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 6, 30, 1, 39043, tzinfo=utc)),
        ),
    ]
