# Generated by Django 3.2.9 on 2021-11-23 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0054_rename_nvr_dvr_nvr_dvrmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projectors',
            new_name='ProjectorModel',
        ),
    ]