# Generated by Django 4.0.2 on 2022-08-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0016_assetmodel_licences'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='nlicences',
            field=models.CharField(default='', max_length=100),
        ),
    ]