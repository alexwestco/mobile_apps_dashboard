# Generated by Django 2.2.3 on 2019-07-25 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_appdownload_continent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appdownload',
            name='continent',
        ),
    ]