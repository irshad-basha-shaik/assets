from django import forms


from django import forms



# creating a form
from .models import AssetModel

USAGE_TYPE = [
    ('Spare_Old', 'Spare_Old'),
    ('Spare_New', 'Spare_New'),
    ('Live','Live'),
]
LOCATION = [
    ('Hyderabad', 'Hyderabad'),
    ('Krishnapatnam', 'Krishnapatnam'),
    ('Kakinada', 'Kakinada'),
    ('Kakinada-3', 'Kakinada-3'),
    ('Marketing', 'Marketing')
]
MACHINE_TYPE = [
    ('Laptop','Laptop'),
    ('Desktop','Desktop'),
    ('Server','Server'),
    ('Workstations','Workstations'),
    ('Cal','Cal'),
    ('Firewall','Firewall'),
    ('VCC','VCC'),
    ('Printers', 'Printer''s'),
    ('UPSs', 'UPS''s'),
    ('Switches','Switches'),
    ('Wifi','Wifi'),
    ('NVR-DVR','NVR-DVR'),
    ('Projector','Projector'),
    ('CCTV Camera','CCTV Camera'),
    ('CCTV-HDD','CCTV-HDD'),
    ('Ext.-HDD','Ext.-HDD'),
    ('NAS','NAS'),
    ('EPBEX','EPBEX'),
    ('Ext.DVD','Ext.DVD'),
    ('Phone','Phone'),
    ('LED-TV','LED-TV'),
    ('Monitor','Monitor'),
    ('Rack','Rack'),
    ('LIUs', 'LIU''s'),
    ('Jackpannel','Jackpannel'),
    ('Camera','Camera'),
    ('Access Control','Access Control'),
    ('Bio-Metric','Bio-Metric'),
    ('Pen-Drive','Pen-Drive'),
    ('Shredding','Shredding'),
]
HDD = [
    ('500MB','500MB'),
    ('120GB', '120GB'),
    ('160GB', '160GB'),
    ('240GB', '240GB'),
    ('500GB', '500GB'),
    ('1TB', '1TB'),
    ('2TB', '2TB'),
    ('10TB', '10TB'),
]
HDD_CAPACITY = (
    ('500MB','500MB'),
    ('120GB', '120GB'),
    ('160GB', '160GB'),
    ('240GB', '240GB'),
    ('500GB', '500GB'),
    ('1TB', '1TB'),
    ('2TB', '2TB'),
    ('10TB', '10TB'),
)
RAM = [
    ('2GB','2GB'),
    ('4GB', '4GB'),
    ('6GB', '6GB'),
    ('8GB', '8GB'),
    ('10GB', '10GB'),
    ('12GB', '12GB'),
    ('16GB', '16GB'),
    ('24GB', '24GB'),
    ('32GB', '32GB'),
    ('64GB', '64GB'),
]
PROCESSOR = [
    ('Dual_Core','Dual_Core'),
    ('Core_I3_1st','Core_I3_1st'),
    ('Core_I3_2nd','Core_I3_2nd'),
    ('Core_I3_3rd','Core_I3_3rd'),
    ('Core_I3_4th','Core_I3_4th'),
    ('Core_I3_10th','Core_I3_10th'),
    ('Core_I5_1st','Core_I5_1st'),
    ('Core_I5_3rd','Core_I5_3rd'),
    ('Core_I5_10th','Core_I5_10th'),
    ('Core_I7_1st','Core_I7_1st'),
    ('Core_I7_3rd','Core_I7_3rd'),
    ('Core_I7_10th','Core_I7_10th')
]
YEARS= [x for x in range(1940,2021)]

MS_VERSION =  (
    ('Office95','Office95'),
    ('Office2000','Office2000'),
    ('Office2003','Office2003'),
    ('Office2007','Office2007'),
    ('Office2010','Office2010'),
    ('Office2013','Office2013'),
    ('Office2016','Office2016'),
    ('Office2019','Office2019'),
    ('Office2022','Office2022')
)
OEM_VOLUME = [x for x in range(1990,2021)]
OS_VERSION = (
    ('Windows XP','Windows XP'),
    ('Windows Vista','Windows Vista'),
    ('Windows 7','Windows 7'),
    ('Windows 8','Windows 8'),
    ('Windows 8.1','Windows 8.1'),
    ('Windows 10','Windows 10'),
    ('Windows 11','Windows 11')
)
OS = (
    ('Windows','Windows'),
    ('Linux','Linux'),
    ('IOS','IOS')
)
DOMAIN_WORKGROUP = (
    ('Domain','Domain'),
    ('Workgroup','Workgroup')
)
REMARKS = (
    ('Under Warranty','Under Warranty'),
    ('Not Working','Not Working'),
    ('Out of Warranty','Out of Warranty')
)
DEVICES = (
    ('Access Point','Access Point'),
    ('Wifi','Wifi')
)
class AssetForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    asset_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    emp_id = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    usage_type = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=USAGE_TYPE))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    gef_id_number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    domain_workgroup = forms.ChoiceField(choices=DOMAIN_WORKGROUP,widget=forms.Select(attrs={'class': 'form-control'}))
    Domain_User_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    hdd_make = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd_model = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd_serial_no =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram =forms.ChoiceField(choices=RAM,widget=forms.Select(attrs={'class': 'form-control'}))
    processor_purchase_date = forms.DateField(label='Processor Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    processor = forms.ChoiceField(choices=PROCESSOR,widget=forms.Select(attrs={'class': 'form-control'}))
    warranty_start_date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    warranty_end_date = forms.DateField(label='Warranty End Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_start_date = forms.DateField(label='AMC Start Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_end_date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    user_acceptance_date = forms.DateField(label='User Acceptance Date', widget=forms.SelectDateWidget(years=YEARS))
    user_handed_over_date = forms.DateField(label='User Handed Over Date', widget=forms.SelectDateWidget(years=YEARS))
    Operating_System_Version = forms.ChoiceField(choices=OS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}))
    OS = forms.ChoiceField(choices=OS,widget=forms.Select(attrs={'class': 'form-control'}))
    ms_office = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    ms_office_version = forms.ChoiceField(choices=MS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}))
    OEM_Volume = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Antivirus = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    AutoCAD = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Adobe_acrobate = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Visio = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Access = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    SAP = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    SAP_User_ID = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = AssetModel
        fields = ['user_name','user_email','location','asset_no','serial_no','emp_id','usage_type','machine_type','gef_id_number','domain_workgroup','Domain_User_Name','machine_make','machine_model_no','machine_serial_no','hdd','hdd_make','hdd_model','hdd_serial_no','ram','processor','processor_purchase_date','warranty_start_date','warranty_end_date','amc_start_date','amc_end_date','user_acceptance_date','user_handed_over_date','ms_office','ms_office_version','OEM_Volume','Operating_System_Version','OS','Antivirus','AutoCAD','Adobe_acrobate','Visio','Access','SAP','SAP_User_ID','Status','Remarks']

class WifiForm(forms.ModelForm):
    Location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asst_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asst_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    User_name_Location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Sl_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Warranty End Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))
    Devices = forms.ChoiceField(choices=DEVICES,widget=forms.Select(attrs={'class': 'form-control'}))

class FirewallForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class VCCForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchased_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Exp_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class PrintersForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchse_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Start_AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    End_AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class UPSForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    User = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchse_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class SwitchesForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    User_name_location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Port = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Devices = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class NVR_DVRForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Installed_Place = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProjectorsForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class CCTV_CameraForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Camera_Type = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Camera_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Camera_Si_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


class CCTV_HDDForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD_Serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD_Capacity = forms.ChoiceField(choices=HDD_CAPACITY,widget=forms.Select(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


class Ext_HDDForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD_Serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    HDD_Capacity = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class NASForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class EPBEXForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Installed_location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class Ext_DVDForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class PhonesForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))


class LED_TVForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    GEF_Allocation_Number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


class MonitorsForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class RacksForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class LIUsForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))

class JackpannelForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Type = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


class CamerasForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_Number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


class Access_ControlForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Installed_location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Serial_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class Bio_MetricForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Serial_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))


class Pen_DrivesForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Old_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    GEF_Allocation_Number_Computer_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    PenDrive_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Start_Date =forms.DateField(label='Warranty_Start_Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_End_Date =forms.DateField(label='Warranty_End_Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='AMC_Start_Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='AMC_End_Date', widget=forms.SelectDateWidget(years=YEARS))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class ShredderForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    New_Asset_No = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Si_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Warranty_Details', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='AMC_Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))
