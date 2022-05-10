# Generated by Django 4.0.2 on 2022-05-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0013_wifi_model_delete_wifimodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wifi_model',
            old_name='Asst_No',
            new_name='asst_no',
        ),
        migrations.RenameField(
            model_name='wifi_model',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='wifi_model',
            old_name='Machine_Model_no',
            new_name='machine_number',
        ),
        migrations.RenameField(
            model_name='wifi_model',
            old_name='Old_Asst_No',
            new_name='old_asst_no',
        ),
        migrations.RenameField(
            model_name='wifi_model',
            old_name='User_name_Location',
            new_name='user_name_location',
        ),
        migrations.RemoveField(
            model_name='wifi_model',
            name='Machine_Number',
        ),
        migrations.RemoveField(
            model_name='wifi_model',
            name='Machine_Sl_no',
        ),
        migrations.RemoveField(
            model_name='wifi_model',
            name='Make',
        ),
        migrations.RemoveField(
            model_name='wifi_model',
            name='Purchase_Date',
        ),
        migrations.RemoveField(
            model_name='wifi_model',
            name='Warranty_Details',
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='AutoCAD_version',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='date_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='machine_age',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='machine_make',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='machine_model_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='machine_serial_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='sub_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wifi_model',
            name='warranty_details',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wifi_model',
            name='AMC_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]