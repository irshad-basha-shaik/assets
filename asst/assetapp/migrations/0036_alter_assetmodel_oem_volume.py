# Generated by Django 3.2.9 on 2021-11-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0035_auto_20211120_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='OEM_Volume',
            field=models.BooleanField(default='1'),
        ),
    ]