# Generated by Django 4.2.4 on 2023-08-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_remove_item_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='People',
            field=models.ManyToManyField(to='mainapp.person'),
        ),
    ]