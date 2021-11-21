# Generated by Django 3.2.9 on 2021-11-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0034_rename_warranty_wnd_date_assetmodel_warranty_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='OEM_Volume',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='OS',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='OS_Version',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='ms_office',
            field=models.BooleanField(default='1'),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='ms_office_version',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
