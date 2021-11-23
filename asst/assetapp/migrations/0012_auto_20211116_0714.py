# Generated by Django 3.2.5 on 2021-11-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0011_auto_20211103_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fruit', models.CharField(max_length=10)),
                ('vegetables', models.CharField(max_length=100)),
                ('location', models.CharField(default='1', max_length=100)),
                ('asset_no', models.CharField(default='1', max_length=100)),
                ('emp_id', models.CharField(default='1', max_length=100)),
                ('usage_type', models.CharField(default='1', max_length=100)),
                ('machine_type', models.CharField(default='1', max_length=100)),
                ('gef_id_number', models.CharField(default='1', max_length=100)),
                ('domain_workgoup', models.CharField(default='1', max_length=100)),
                ('make1', models.CharField(default='1', max_length=100)),
                ('machine_model_no', models.CharField(default='1', max_length=100)),
                ('serial_no1', models.CharField(default='1', max_length=100)),
                ('hdd', models.CharField(default='1', max_length=100)),
                ('make2', models.CharField(default='1', max_length=100)),
                ('model', models.CharField(default='1', max_length=100)),
                ('serial_no2', models.CharField(default='1', max_length=100)),
                ('ram', models.CharField(default='1', max_length=100)),
                ('processor_purchase_date', models.CharField(default='1', max_length=100)),
                ('warranty_end_date', models.CharField(default='1', max_length=100)),
                ('amc_start_date', models.CharField(default='1', max_length=100)),
                ('amc_end_date', models.CharField(default='1', max_length=100)),
                ('os_version', models.CharField(default='1', max_length=100)),
                ('os', models.CharField(default='1', max_length=100)),
                ('ms_office_version', models.CharField(default='1', max_length=100)),
                ('oem', models.CharField(default='1', max_length=100)),
                ('antivirus', models.CharField(default='1', max_length=100)),
                ('autocad', models.CharField(default='1', max_length=100)),
                ('adobe_acrobate', models.CharField(default='1', max_length=100)),
                ('visio', models.CharField(default='1', max_length=100)),
                ('access', models.CharField(default='1', max_length=100)),
                ('sap', models.CharField(default='1', max_length=100)),
                ('status', models.CharField(default='1', max_length=100)),
                ('remarks', models.CharField(default='1', max_length=100)),
                ('user_acceptance_date', models.CharField(default='1', max_length=100)),
                ('user_handed_over_date', models.CharField(default='1', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Acategory',
        ),
        migrations.DeleteModel(
            name='Assets',
        ),
        migrations.DeleteModel(
            name='Assets_types',
        ),
        migrations.DeleteModel(
            name='Astatus',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Ops',
        ),
        migrations.DeleteModel(
            name='Software',
        ),
    ]