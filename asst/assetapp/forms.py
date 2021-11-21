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
class AssetForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    asset_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    emp_id = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    usage_type = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=USAGE_TYPE))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    gef_id_number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    domain_workgroup = forms.ChoiceField(choices=DOMAIN_WORKGROUP,widget=forms.Select(attrs={'class': 'form-control'}))
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
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Remarks =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AssetModel
        fields = ['user_name','location','asset_no','serial_no','emp_id','usage_type','machine_type','gef_id_number','domain_workgroup','machine_make','machine_model_no','machine_serial_no','hdd','hdd_make','hdd_model','hdd_serial_no','ram','processor','processor_purchase_date','warranty_start_date','warranty_end_date','amc_start_date','amc_end_date','user_acceptance_date','user_handed_over_date','ms_office','ms_office_version','OEM_Volume','Operating_System_Version','OS','Antivirus','AutoCAD','Adobe_acrobate','Visio','Access','SAP','Status','Remarks']