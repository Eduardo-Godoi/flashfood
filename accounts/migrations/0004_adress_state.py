# Generated by Django 3.2.9 on 2021-12-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211202_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='state',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]