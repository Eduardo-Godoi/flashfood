# Generated by Django 3.2.9 on 2021-11-27 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAdress',
            new_name='Adress',
        ),
    ]
