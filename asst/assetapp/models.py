
from django.db import models
from datetime import date

class AssetModel(models.Model):
    location = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100, default='1')
    emp_id = models.CharField(max_length=100, default='1')
    usage_type = models.CharField(max_length=100, default='1')
    machine_type = models.CharField(max_length=100, default='1')
    gef_id_number = models.CharField(max_length=100, default='1')
    domain_workgoup = models.CharField(max_length=100, default='1')
    machine_make = models.CharField(max_length=100, default='1')
    machine_model_no = models.CharField(max_length=100, default='1')
    machine_serial_no = models.CharField(max_length=100, default='1')
    hdd = models.CharField(max_length=100, default='1')
    hdd_make = models.CharField(max_length=100, default='1')
    hdd_model = models.CharField(max_length=100, default='1')
    hdd_serial_no = models.CharField(max_length=100, default='1')
    ram = models.CharField(max_length=100, default='1')
    processor = models.CharField(max_length=100, default='1')
    processor_purchase_date = models.DateField(default=date(1111, 11, 11))
    warranty_start_date = models.DateField(default=date(1111, 11, 11))
    warranty_end_date = models.DateField(default=date(1111, 11, 11))
    amc_start_date = models.DateField(default=date(1111, 11, 11))
    amc_end_date = models.DateField(default=date(1111, 11, 11))
    user_acceptance_date = models.DateField(default=date(1111, 11, 11))
    user_handed_over_date = models.DateField(default=date(1111, 11, 11))
    OS_Version = models.CharField(max_length=100, default='1')
    OS = models.CharField(max_length=100, default='1')
    ms_office = models.BooleanField(default='1')
    ms_office_version = models.CharField(max_length=100, default='1')
    OEM_Volume = models.CharField(max_length=100, default='1')


