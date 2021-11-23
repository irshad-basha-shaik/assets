# Generated by Django 3.2.9 on 2021-11-22 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0048_auto_20211122_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('Installed_location', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('Serial_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bio_Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('Serial_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_Number', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CCTV_Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Camera_Type', models.CharField(max_length=100)),
                ('Camera_Model_no', models.CharField(max_length=100)),
                ('Camera_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CCTV_HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('HDD', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('HDD_Serial_no', models.CharField(max_length=100)),
                ('HDD_Capacity', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EPBEX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('Installed_location', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ext_DVD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('Serial_no', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ext_HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('HDD_Model_no', models.CharField(max_length=100)),
                ('HDD_Serial_no', models.CharField(max_length=100)),
                ('HDD_Capacity', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FirewallModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asst_No', models.CharField(max_length=100)),
                ('Asst_No', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jackpannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LED_TV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset', models.CharField(max_length=100)),
                ('New_Asset', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('GEF_Allocation_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LIUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset', models.CharField(max_length=100)),
                ('New_Asset', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NVR_DVR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_no', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('Installed_Place', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pen_Drives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('PenDrive_Model_no', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Printers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('New_Asset_No', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchse_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Start_AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('End_AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('New_Asset_No', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Racks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('GEF_Allocation_Number_Computer_Name', models.CharField(max_length=100)),
                ('Warranty_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shredder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('New_Asset_No', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Old_Asset_No', models.CharField(max_length=100)),
                ('Asset_No', models.CharField(max_length=100)),
                ('User_name_Location', models.CharField(max_length=100)),
                ('Port', models.CharField(max_length=100)),
                ('Devices', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchase_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Asset_no', models.CharField(max_length=100)),
                ('New_Asset_No', models.CharField(max_length=100)),
                ('User', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_no', models.CharField(max_length=100)),
                ('Machine_Number', models.CharField(max_length=100)),
                ('Purchse_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Details', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VCCModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('Asst_No', models.CharField(max_length=100)),
                ('Machine_Type', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Machine_Model_no', models.CharField(max_length=100)),
                ('Machine_Si_No', models.CharField(max_length=100)),
                ('Purchased_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Warranty_Exp_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_Start_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('AMC_End_Date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
