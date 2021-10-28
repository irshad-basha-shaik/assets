from django.db import models

# create your models here.
class Assets(models.Model):
    location = models.CharField(max_length=100)
    asset_no = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    usage_type = models.CharField(max_length=100)
    machine_type = models.CharField(max_length=100)
    gef_identification_number = models.CharField(max_length=100)
    domain_workgoup = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    machine_model_no = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    hdd = models.CharField(max_length=100)
    make1 = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    purchase_date = models.CharField(max_length=100)
    warranty_start_date = models.CharField(max_length=100)
    warranty_end_date = models.CharField(max_length=100)
    amc_start_date = models.CharField(max_length=100)
    amc_end_date = models.CharField(max_length=100)
    os_version = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    ms_office_version = models.CharField(max_length=100)
    ms_office_version1 = models.CharField(max_length=100)
    os_details = models.CharField(max_length=100)
    antivirus = models.CharField(max_length=100)
    autocad = models.CharField(max_length=100)
    adobe_acrobate = models.CharField(max_length=100)
    visio = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    sap = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    user_acceptance_date = models.CharField(max_length=100)
    user_handed_over_date = models.CharField(max_length=100)


class meta:
        db_table='assets'

class Assets_types(models.Model):
    dname=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    class meta:
        db_table='assets_types'
