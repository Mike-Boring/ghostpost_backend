# Generated by Django 3.1.1 on 2020-10-01 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200930_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastsroasts',
            name='total_votes',
        ),
    ]
