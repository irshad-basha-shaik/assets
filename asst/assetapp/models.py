
from django.db import models
from django.urls import reverse
from datetime import date
from django.core.mail import EmailMessage
import datetime
from django.conf import settings
from django.utils import dateformat
from django.utils.timesince import timesince
#import tensorflow as tf

class AssetModel(models.Model):
    user_name = models.CharField(max_length=100, default='')
    user_contact = models.CharField(max_length=100, default='')
    user_email = models.EmailField(max_length=100,default='')
    location = models.CharField(max_length=100)
    sub_location = models.CharField(max_length=100,default='')
    asset_no = models.CharField(max_length=100, default='')
    serial_no = models.CharField(max_length=100, default='')
    emp_id = models.CharField(max_length=100, default='')
    usage_type = models.CharField(max_length=100, default='')
    machine_type = models.CharField(max_length=100, default='')
    gef_id_number = models.CharField(max_length=100, default='')
    domain_workgroup = models.CharField(max_length=100, default='')
    Domain_User_Name = models.CharField(max_length=100, default='')
    machine_make = models.CharField(max_length=100, default='')
    machine_age = models.CharField(max_length=100, default='')
    machine_model_no = models.CharField(max_length=100, default='')
    machine_serial_no = models.CharField(max_length=100, default='')
    hdd = models.CharField(max_length=100, default='')
    hdd_type = models.CharField(max_length=100, default='')
    hdd_make = models.CharField(max_length=100, default='')
    hdd_model = models.CharField(max_length=100, default='')
    hdd_serial_no = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=100, default='')
    processor = models.CharField(max_length=100, default='')
    processor_purchase_date = models.DateField(null=True,blank=True)
    date_type = models.CharField(max_length=100, default='')
    amc_start_date = models.DateField(null=True,blank=True)
    amc_end_date = models.DateField(null=True,blank=True)
    user_acceptance_date = models.DateField(null=True,blank=True)
    user_handed_over_date = models.DateField(null=True,blank=True)
    Operating_System_Version = models.CharField(max_length=100, default='')
    OS = models.CharField(max_length=100, default='')
    OS_type = models.CharField(max_length=100, default='')
    OEM_Volume = models.CharField(max_length=100, default='')
    ms_office = models.BooleanField(default='')
    ms_office_version = models.CharField(max_length=100, default='')
    ms_365 = models.CharField(max_length=100, default='')
    ms_visio = models.CharField(max_length=100, default='')
    ms_access = models.CharField(max_length=100, default='')
    Antivirus = models.BooleanField(default='')
    AutoCAD = models.BooleanField(default='')
    AutoCAD_version = models.CharField(max_length=100, default='')
    Coral_Draw = models.BooleanField(default='')
    Pdf_Writer = models.BooleanField(default='')
    Winzip = models.BooleanField(default='')
    Installed_Softwares = models.CharField(max_length=1000, default='')
    Adobe_acrobate = models.BooleanField(default='')
    Visio = models.BooleanField(default='')
    Access = models.BooleanField(default='')
    SAP = models.BooleanField(default='')
    SAP_User_ID =models.CharField(max_length=100, default='')
    Status = models.CharField(max_length=100, default='')
    Remarks = models.CharField(max_length=100, default='')

    def get_time_diff(self):
        if self.processor_purchase_date==None:
            self.processor_purchase_date = date.today()
            return timesince(self.processor_purchase_date)
        else:
            return timesince(self.processor_purchase_date)
    def get_day_diff(self):
        if self.amc_end_date!=None:
            remaining = (self.amc_end_date - date.today()).days
            if remaining >0:
                if remaining <= 91:
                    return remaining

class LicenceModel(models.Model):
    Licences = models.CharField(max_length=100, default='')
    nlicences = models.CharField(max_length=100, default='')

class Nlicence(models.Model):
    new_licence=models.CharField(max_length=100)
    class Meta:
        db_table='Nlicence'

class PingModel(models.Model):
    Ip_Address = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Alert_Range = models.CharField(max_length=100)
    Last_Updated = models.CharField(max_length=100,default="")


    def __str__(self):
        return self.Ip_Address,self.Name,self.Status,self.Alert_Range

    def get_absolute_url(self):
        return reverse('pingmodel-detail', kwargs={'pk': self.pk})



class Wifi_Model(models.Model):
    location = models.CharField(max_length=100)
    sub_location = models.CharField(max_length=100, default='')
    old_asst_no = models.CharField(max_length=100)
    asst_no = models.CharField(max_length=100)
    user_name_location = models.CharField(max_length=100)
    machine_make = models.CharField(max_length=100, default='')
    machine_age = models.CharField(max_length=100, default='')
    machine_model_no = models.CharField(max_length=100, default='')
    machine_serial_no = models.CharField(max_length=100, default='')
    machine_number = models.CharField(max_length=100)
    purchase_date = models.DateField(null=True,blank=True)
    warranty_details = models.DateField(null=True,blank=True)
    AMC_Date = models.DateField(null=True,blank=True)
    date_type = models.CharField(max_length=100, default='')
    Remarks = models.CharField(max_length=100)
    Devices = models.CharField(max_length=100,default='1')





'''
class FirewallModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asst_No = models.CharField(max_length=100)
    Asst_No = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Sl_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    AMC_Start_Date = models.DateField(default=date(1111, 11, 11))
    AMC_End_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)

class VCCModel(models.Model):
    Location = models.CharField(max_length=100)
    Asst_No = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_No = models.CharField(max_length=100)
    Purchased_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Exp_Date = models.DateField(default=date(1111, 11, 11))
    AMC_Start_Date = models.DateField(default=date(1111, 11, 11))
    AMC_End_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)

class PrinterModel(models.Model):
    Location = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    New_Asset_No = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchse_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    Start_AMC_Date = models.DateField(default=date(1111, 11, 11))
    End_AMC_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)

class UPSModel(models.Model):
    Location = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    New_Asset_No = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchse_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)

class SwitcheModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_No = models.CharField(max_length=100)
    User_name_Location = models.CharField(max_length=100)
    Port = models.CharField(max_length=100)
    Devices = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)

class NVR_DVRModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_no = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    Installed_Place = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class ProjectorModel(models.Model):
    Location = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    New_Asset_No = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Machine_Number1 = models.CharField(max_length=100,default='1')
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)

class CCTV_CameraModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Camera_Type = models.CharField(max_length=100)
    Camera_Model_no = models.CharField(max_length=100)
    Camera_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)


class CCTV_HDDModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    HDD = models.CharField(max_length=100)
    Model_no = models.CharField(max_length=100)
    HDD_Serial_no = models.CharField(max_length=100)
    HDD_Capacity = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)


class Ext_HDDModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    HDD_Model_no = models.CharField(max_length=100)
    HDD_Serial_no = models.CharField(max_length=100)
    HDD_Capacity = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class NASModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)

class EPBEXModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    Installed_location =models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class Ext_DVDModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Model_no = models.CharField(max_length=100)
    Serial_no =models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class PhonesModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)


class LED_TVModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset =models.CharField(max_length=100)
    New_Asset =models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    GEF_Allocation_Number =models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)


class MonitorsModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset =models.CharField(max_length=100)
    New_Asset =models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)

class RacksModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name = models.CharField(max_length=100)
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class LIUsModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)

class JackpannelModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)


class CamerasModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_Number = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)


class Access_ControlModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    Installed_location =models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Model_no = models.CharField(max_length=100)
    Serial_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class Bio_MetricModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Model_no = models.CharField(max_length=100)
    Serial_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)


class Pen_DrivesModel(models.Model):
    Location = models.CharField(max_length=100)
    Old_Asset_No = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    GEF_Allocation_Number_Computer_Name =models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    PenDrive_Model_no = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Start_Date =models.DateField(default=date(1111, 11, 11))
    Warranty_End_Date =models.DateField(default=date(1111, 11, 11))
    AMC_Start_date = models.DateField(default=date(1111, 11, 11))
    AMC_End_date = models.DateField(default=date(1111, 11, 11))
    Status = models.CharField(max_length=100)

class ShredderModel(models.Model):
    Location = models.CharField(max_length=100)
    Asset_no = models.CharField(max_length=100)
    New_Asset_No = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Machine_Type = models.CharField(max_length=100)
    Machine_Model_no = models.CharField(max_length=100)
    Machine_Si_no = models.CharField(max_length=100)
    Machine_Number = models.CharField(max_length=100)
    Purchase_Date = models.DateField(default=date(1111, 11, 11))
    Warranty_Details = models.DateField(default=date(1111, 11, 11))
    AMC_Date = models.DateField(default=date(1111, 11, 11))
    Remarks = models.CharField(max_length=100)
'''


