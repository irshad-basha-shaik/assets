# Generated by Django 4.0.2 on 2022-03-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0080_alter_assetmodel_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='emp_id',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
