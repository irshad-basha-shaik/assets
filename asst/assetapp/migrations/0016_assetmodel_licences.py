# Generated by Django 4.0.2 on 2022-08-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0015_assetmodel_os_type_alter_assetmodel_oem_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='Licences',
            field=models.CharField(default='', max_length=100),
        ),
    ]
