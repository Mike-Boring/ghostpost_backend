# Generated by Django 3.1.1 on 2020-10-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_boastsroasts_total_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='boastsroasts',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]
