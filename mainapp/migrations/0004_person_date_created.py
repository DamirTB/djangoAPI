# Generated by Django 4.2.4 on 2023-08-15 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_person_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 8, 15, 22, 52, 26, 115406)),
        ),
    ]