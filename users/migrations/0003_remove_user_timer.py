# Generated by Django 2.2.24 on 2021-08-03 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210730_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timer',
        ),
    ]
