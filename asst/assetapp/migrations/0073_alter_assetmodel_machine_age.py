# Generated by Django 4.0.1 on 2022-02-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0072_alter_assetmodel_machine_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='machine_age',
            field=models.CharField(default='', max_length=100),
        ),
    ]
