# Generated by Django 4.0.2 on 2022-02-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0069_remove_assetmodel_email_type_assetmodel_coral_draw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='ms_access',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='ms_visio',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='user_contact',
            field=models.CharField(default='', max_length=100),
        ),
    ]
