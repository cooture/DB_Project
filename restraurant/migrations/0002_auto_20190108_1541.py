# Generated by Django 2.1.5 on 2019-01-08 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restraurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authgroup',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'managed': True},
        ),
    ]