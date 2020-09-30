# Generated by Django 3.1.1 on 2020-09-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200929_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastsroasts',
            name='boasts',
        ),
        migrations.AlterField(
            model_name='boastsroasts',
            name='post_type',
            field=models.CharField(choices=[('boast', 'Boast'), ('roast', 'Roast')], default='Boast', max_length=32),
        ),
    ]