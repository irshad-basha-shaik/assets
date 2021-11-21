# Generated by Django 3.2.5 on 2021-11-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0009_alter_ops_ms_office_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='access',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='adobe_acrobate',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='antivirus',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='autocad',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='sap',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='serial_no1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='visio',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
