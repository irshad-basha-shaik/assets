from django import forms


from django import forms



# creating a form
from .models import AssetModel,WifiModel,FirewallModel,VCCModel

USAGE_TYPE = [
    ('Spare_Old', 'Spare_Old'),
    ('Spare_New', 'Spare_New'),
    ('Live','Live'),
]
LOCATION = [
    ('HYDERABAD', 'HYDERABAD'),
    ('KRISHNAPATNAM', 'KRISHNAPATNAM'),
    ('KAKINADA', 'KAKINADA'),
    ('KAKINADA-3', 'KAKINADA-3'),
    ('MARKETING', 'MARKETING'),
    ('DEPOT', 'DEPOT')

]

MACHINE_TYPE = [
    ('Laptop','Laptop'),
    ('Desktop','Desktop'),
    ('Server','Server'),

]
HDD = [
    ('160 GB', '160 GB'),
    ('120 SSD', '120 SSD'),
    ('240 GB', '240 GB'),
    ('250 GB', '250 GB'),
    ('256 SSD', '256 SSD'),
    ('320 GB', '320 GB'),
    ('350 GB', '350 GB'),
    ('500 GB', '500 GB'),
    ('512 GB', '512 GB'),
    ('512 GB SSD', '512 GB SSD'),
    ('1 TB', '1 TB'),
    ('1 TB SSD', '1 TB SSD'),
    ('1 TB  SSD', '1 TB SSD'),
    ('1 TB+256 SSD', '1 TB+256 SSD'),
    ('1TB+256GB', '1 TB+256 SSD'),
    ('1 TB+256 GB SSD', '1 TB+256 GB SSD'),
    ('1 TB 256 GB SSD', '1 TB+256 GB SSD'),
    ('256 SSD+1 TB', '256 SSD+1 TB'),
    ('2 TB', '2 TB'),
    ('2 TB SSD', '2 TB SSD'),
    ('2TB+4TB', '2TB+4TB'),
    ('', ''),

]
HDD_CAPACITY = (
    ('500MB','500MB'),
    ('120GB', '120GB'),
    ('160GB', '160GB'),
    ('240GB', '240GB'),
    ('350GB', '350GB'),
    ('350 GB', '350 GB'),
    ('500GB', '500GB'),
    ('1TB', '1TB'),
    ('2TB', '2TB'),
    ('10TB', '10TB'),
)
RAM = [
    ('2 GB','2 GB'),
    ('3 GB','3 GB'),
    ('4 GB', '4 GB'),
    ('6 GB', '6 GB'),
    ('8 GB', '8 GB'),
    ('10 GB', '10 GB'),
    ('12 GB', '12 GB'),
    ('16 GB', '16 GB'),
    ('24 GB', '24 GB'),
    ('32 GB', '32 GB'),
    ('64 GB', '64 GB'),
    ('', ''),
]
PROCESSOR = [
    ('Core i-3', 'Core i-3'),
    ('Core i-3 2.00 GHz', 'Core i-3 2.00 GHz'),
    ('Core i-3 2.40 GHZ', 'Core i-3 2.40 GHZ'),
    ('Core i-3 3.70 GHZ', 'Core i-3 3.70 GHZ'),
    ('Core i-3, 2.10 GHZ', 'Core i-3, 2.10 GHZ'),
    ('Core i-5', 'Core i-5'),
    ('Core i-5 1.60 Ghz', 'Core i-5 1.60 Ghz'),
    ('Core i-5 1.80 Ghz', 'Core i-5 1.80 Ghz'),
    ('Core i-5 2.19 GHZ', 'Core i-5 2.19 GHZ'),
    ('Core i-5 2.20 GHZ', 'Core i-5 2.20 GHZ'),
    ('Core i-5 2.20GHZ', 'Core i-5 2.20GHZ'),
    ('Core i-5 2.30 GHZ', 'Core i-5 2.30 GHZ'),
    ('Core i-5 2.40 GHZ', 'Core i-5 2.40 GHZ'),
    ('Core I-5 2.40 Ghz', 'Core I-5 2.40 Ghz'),
    ('Core i-5 2.40 Ghz', 'Core i-5 2.40 Ghz'),
    ('Core i-5 2.50 GHZ', 'Core i-5 2.50 GHZ'),
    ('Core i-5, 1.60 GHz', 'Core i-5, 1.60 GHz'),
    ('Core i-5, 2.11 GHz', 'Core i-5, 2.11 GHz'),
    ('Core i-5, 2.18 GHz', 'Core i-5, 2.18 GHz'),
    ('Core i-5, 2.20 GHz', 'Core i-5, 2.20 GHz'),
    ('Core I-5, 2.40 GHz', 'Core I-5, 2.40 GHz'),
    ('Core i-5, 2.50 GHZ', 'Core i-5, 2.50 GHZ'),
    ('Core i-5, 2.50 GHz', 'Core i-5, 2.50 GHz'),
    ('Core i-5, 2.60 GHZ', 'Core i-5, 2.60 GHZ'),
    ('Core i-5, 2.60 GHz', 'Core i-5, 2.60 GHz'),
    ('Core i-5, 2.70 GHZ', 'Core i-5, 2.70 GHZ'),
    ('Core i-5, 3.20 GHz', 'Core i-5, 3.20 GHz'),
    ('core i-5, 3.20 Ghz', 'core i-5, 3.20 Ghz'),
    ('core i-5, 3.20 GHz', 'core i-5, 3.20 GHz'),
    ('Core i-5,2.20 GHz', 'Core i-5,2.20 GHz'),
    ('core i-5,2.60 GHz', 'core i-5,2.60 GHz'),
    ('Core i-7', 'Core i-7'),
    ('Core I-7 1.80 GHz', 'Core I-7 1.80 GHz'),
    ('Core i-7 1.90 GHz', 'Core i-7 1.90 GHz'),
    ('Core I-7 1.90 GHz', 'Core I-7 1.90 GHz'),
    ('Core i-7, 2.30 GHz', 'Core i-7, 2.30 GHz'),
    ('Core i-7, 2.90 GHz', 'Core i-7, 2.90 GHz'),
    ('Core i-7,1.19 GHz', 'Core i-7,1.19 GHz'),
    ('Core i3  3.60 GHz', 'Core i3  3.60 GHz'),
    ('Core i3  3.70 GHz', 'Core i3  3.70 GHz'),
    ('Core i5  1.60GHz', 'Core i5  1.60GHz'),
    ('Core i5  2.20GHz', 'Core i5  2.20GHz'),
    ('Core i5 2.20 GHZ', 'Core i5 2.20 GHZ'),
    ('Core i5 2.20 GHz', 'Core i5 2.20 GHz'),
    ('Core i5 2.50 GHZ', 'Core i5 2.50 GHZ'),
    ('Core i5 2.60 GHz', 'Core i5 2.60 GHz'),
    ('Core i5 2.90 GHZ', 'Core i5 2.90 GHZ'),
    ('Core i5 3.2 GHZ', 'Core i5 3.2 GHZ'),
    ('Core i5 3.20 GHz', 'Core i5 3.20 GHz'),
    ('core i5 3.30 GHZ', 'core i5 3.30 GHZ'),
    ('Core i5 3.7GHz', 'Core i5 3.7GHz'),
    ('Core i5 4.1GHz', 'Core i5 4.1GHz'),
    ('Core i5, 1.80 GHz', 'Core i5, 1.80 GHz'),
    ('Core i5-2.20 GHZ', 'Core i5-2.20 GHZ'),
    ('Core i5-2.40 GHZ', 'Core i5-2.40 GHZ'),
    ('Core i5-2.50 GHZ', 'Core i5-2.50 GHZ'),
    ('Core i5-2.60 GHZ', 'Core i5-2.60 GHZ'),
    ('Core I5-6th 2.3 Ghz', 'Core I5-6th 2.3 Ghz'),
    ('Core-i-7,  2.30 GHz', 'Core-i-7,  2.30 GHz'),
    ('Core-i3 8thgen', 'Core-i3 8thgen'),
    ('Core-i5', 'Core-i5'),
    ('Core-i5  1.60GHz', 'Core-i5  1.60GHz'),
    ('Core-i5  2.20GHz', 'Core-i5  2.20GHz'),
    ('Core-i5  2.50GHz', 'Core-i5  2.50GHz'),
    ('Core-i5  2.60GHz', 'Core-i5  2.60GHz'),
    ('Core-i5  3.20GHz', 'Core-i5  3.20GHz'),
    ('Core-i5  3.90GHz', 'Core-i5  3.90GHz'),
    ('Core-i5 10th gen', 'Core-i5 10th gen'),
    ('Core-i5 11th gen', 'Core-i5 11th gen'),
    ('Core-i5 2.20GHz', 'Core-i5 2.20GHz'),
    ('Core-i5 2.30GHz', 'Core-i5 2.30GHz'),
    ('Core-i5 2.50 GHZ', 'Core-i5 2.50 GHZ'),
    ('CORE-i5 3.90 GHZ', 'CORE-i5 3.90 GHZ'),
    ('Core-i5 7thgen', 'Core-i5 7thgen'),
    ('Core-i5 8thgen', 'Core-i5 8thgen'),
    ('Core-i7  1.80GHz', 'Core-i7  1.80GHz'),
    ('Core-i7 10th gen', 'Core-i7 10th gen'),
    ('Core2dual 2.40 GHz', 'Core2dual 2.40 GHz'),
    ('Core2Dual 2.93 GHz', 'Core2Dual 2.93 GHz'),
    ('Core2Duo 2.40 Ghz', 'Core2Duo 2.40 Ghz'),
    ('Core2Duo 2.93 Ghz', 'Core2Duo 2.93 Ghz'),
    ('Core2Duo 2.93 GHz', 'Core2Duo 2.93 GHz'),
    ('Core2Duo 3.30 Ghz', 'Core2Duo 3.30 Ghz'),
    ('Core2Duo-2.40 GHZ', 'Core2Duo-2.40 GHZ'),
    ('Core2Duo-2.93 GHZ', 'Core2Duo-2.93 GHZ'),
    ('Corei-5 1.60 GHz', 'Corei-5 1.60 GHz'),
    ('Corei-5 2.50 GHz', 'Corei-5 2.50 GHz'),
    ('Corei3 3.60 GHz', 'Corei3 3.60 GHz'),
    ('Corei3 3.70GHz', 'Corei3 3.70GHz'),
    ('Corei3-3.10 GHZ', 'Corei3-3.10 GHZ'),
    ('Corei3-3.30 GHZ', 'Corei3-3.30 GHZ'),
    ('Corei3-3.7 GHZ', 'Corei3-3.7 GHZ'),
    ('Corei3-6100-3.70GHZ', 'Corei3-6100-3.70GHZ'),
    ('Corei5 3.30 GHz', 'Corei5 3.30 GHz'),
    ('Corei5-4590-3.30GHZ', 'Corei5-4590-3.30GHZ'),
    ('Corei5-6500-3.20GHZ', 'Corei5-6500-3.20GHZ'),
    ('Corei5-9500, 3.2GHZ', 'Corei5-9500, 3.2GHZ'),
    ('i-3, 2.30Ghz', 'i-3, 2.30Ghz'),
    ('I-5 3.20 Ghz', 'I-5 3.20 Ghz'),
    ('I-7, 1.90 Ghz', 'I-7, 1.90 Ghz'),
    ('i3 3.6 GHZ', 'i3 3.6 GHZ'),
    ('i3 3.9 GHZ', 'i3 3.9 GHZ'),
    ('I3-7th Gen 3.7 Ghz', 'I3-7th Gen 3.7 Ghz'),
    ('I3-7th Gen 3.9 Ghz', 'I3-7th Gen 3.9 Ghz'),
    ('I3-8th Gen 3.6 Ghz', 'I3-8th Gen 3.6 Ghz'),
    ('I5 processor', 'I5 processor'),
    ('I5, Gen 3.0 Ghz', 'I5, Gen 3.0 Ghz'),
    ('I5-7th Gen', 'I5-7th Gen'),
    ('I5-8th Gen', 'I5-8th Gen'),
    ('I5-8th Gen 3.0 Ghz', 'I5-8th Gen 3.0 Ghz'),
    ('I5-8th Gen 3.0Ghz', 'I5-8th Gen 3.0Ghz'),
    ('I7-9th Gen 3.0Ghz to 4.7Ghz', 'I7-9th Gen 3.0Ghz to 4.7Ghz'),
    ('I7-9th Gen 4.7 Ghz', 'I7-9th Gen 4.7 Ghz'),
    ('Intel Xeon Silver 4110 2.10GHZ', 'Intel Xeon Silver 4110 2.10GHZ'),
    ('InteL- 3.10 Ghz', 'InteL- 3.10 Ghz'),
    ('InteL- 3.50 Ghz', 'InteL- 3.50 Ghz'),
    ('Intel®Xeon 3.50GHZ', 'Intel®Xeon 3.50GHZ'),
    ('P Dualcore-3 GHZ', 'P Dualcore-3 GHZ')

]
YEARS= [x for x in range(1940,2021)]

Email_Type = (
    ('O365', 'O365'),
    ('Zimbra', 'Zimbra'),
    ('Public', 'Public'),
)

MS_VERSION =  (
    ('MS Office Standard 2010', 'MS Office Standard 2010'),
    ('MS Office Standard 2013', 'MS Office Standard 2013'),
    ('MS Office Standard 2016', 'MS Office Standard 2016'),
    ('MS Office Standard 2019', 'MS Office Standard 2019'),
    ('','')
)
VISIO_VERSION =  (
    ('MS Visio 2010', 'MS Visio 2010'),
    ('MS Visio 2013', 'MS Visio 2013'),
    ('MS Visio 2016', 'MS Visio 2016'),
    ('MS Visio 2019', 'MS Visio 2019'),
    ('','')
)
ACCESS_VERSION =  (
    ('MS Access 2010', 'MS Access 2010'),
    ('MS Access 2013', 'MS Access 2013'),
    ('MS Access 2016', 'MS Access 2016'),
    ('MS Access 2019', 'MS Access 2019'),
    ('','')
)
OEM_VOLUME = [x for x in range(1990,2021)]
OS_VERSION = (
    ('',''),
    ('Win-7 Pro.32 Bit','Win-7 Pro.32 Bit'),
    ('Win-Server-2012','Win-Server-2012'),
    ('Win-10 Pro 64 Bit','Win-10 Pro 64 Bit'),
    ('Win-8.1 Pro.32 Bit','Win-8.1 Pro.32 Bit'),
    ('Win-8.1 Pro 64 Bit','Win-8.1 Pro 64 Bit'),
    ('Win-10 Pro. 32 Bit','Win-10 Pro. 32 Bit'),
    ('Win-7 Pro.64 Bit','Win-7 Pro.64 Bit'),
    ('Win.10 pro. 64 Bit','Win.10 pro. 64 Bit'),
    ('Win-8.1pro 64 Bit','Win-8.1pro 64 Bit'),
    ('Win-8.1 Pro 32 Bit','Win-8.1 Pro 32 Bit'),
    ('windows 10Pro.64bit','windows 10Pro.64bit'),
    ('Win- 8.1Pro.64bit','Win- 8.1Pro.64bit'),
    ('Win- 8.1 Pro 64 Bit','Win- 8.1 Pro 64 Bit'),
    ('Win-8.1 Pro.64 Bit','Win-8.1 Pro.64 Bit'),
    ('Windows 10Pro.64bit','Windows 10Pro.64bit'),
    ('Windows Xp Pro.','Windows Xp Pro.'),
    ('Win-8.1Pro 32 Bit','Win-8.1Pro 32 Bit'),
    ('Windows 10 Pro 64 Bit','Windows 10 Pro 64 Bit'),
    ('Win-Server-2016 Std','Win-Server-2016 Std'),
    ('Win-10 Home Single Lan.','Win-10 Home Single Lan.'),
    ('Win-10 Pro 64 bit','Win-10 Pro 64 bit'),

)
OS = (
    ('Win.XP', 'Win.XP'),
    ('Win.7', 'Win.7'),
    ('Win.8', 'Win.8'),
    ('Win.10', 'Win.10'),
    ('Win.11', 'Win.11'),
    ('Ser.2012', 'Ser.2012'),
    ('Ser.2016', 'Ser.2016'),
    ('Ser.2019', 'Ser.2019'),
    ('', ''),
)
AVAILABLE_LICENCE={
    'Win.7': 56,
    'Win.8': 85,
    'Win.10': 188,
    'Win.11': 0,
    'Ser.2012': 9,
    'Ser.2016': 1,
    'Ser.2019': 0,
    'Win.XP': 5,
    'MS Office Standard 2010': 55,
    'MS Office Standard 2013': 85,
    'MS Office Standard 2016':130,
    'MS Office Standard 2019': 40,
    'MS Office 365': 28
}
AVAILABLE_LICENCE_ORDER={
    'Win.7': 1.2,
    'Win.8': 1.3,
    'Win.10': 1.4,
    'Win.11': 1.5,
    'Ser.2012': 2.1,
    'Ser.2016': 2.2,
    'Ser.2019': 2.3,
    'Win.XP': 1.1,
    'MS Office Standard 2010': 4.1,
    'MS Office Standard 2013': 4.2,
    'MS Office Standard 2016':4.3,
    'MS Office Standard 2019': 4.4
}
DOMAIN_WORKGROUP = (
    ('Domain','Domain'),
    ('Workgroup','Workgroup'),
    ('', '')

)
REMARKS = (
    ('Spare','Spare'),
    ('Used','Used'),
    ('Not Working','Not Working')
)
DEVICES = (
    ('Access Point','Access Point'),
    ('Wifi','Wifi')
)


class AssetForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    user_email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}),required=False)
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    asset_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    emp_id = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    usage_type = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=USAGE_TYPE))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    gef_id_number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    domain_workgroup = forms.ChoiceField(choices=DOMAIN_WORKGROUP,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    Domain_User_Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    hdd = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    hdd_make = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    hdd_model = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    hdd_serial_no =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    ram =forms.ChoiceField(choices=RAM,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    processor_purchase_date = forms.DateField(label='Processor Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    processor = forms.ChoiceField(choices=PROCESSOR,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    warranty_start_date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    warranty_end_date = forms.DateField(label='Warranty End Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_start_date = forms.DateField(label='AMC Start Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_end_date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    user_acceptance_date = forms.DateField(label='User Acceptance Date', widget=forms.SelectDateWidget(years=YEARS))
    user_handed_over_date = forms.DateField(label='User Handed Over Date', widget=forms.SelectDateWidget(years=YEARS))
    Operating_System_Version = forms.ChoiceField(choices=OS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    OS = forms.ChoiceField(choices=OS,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    ms_office = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    ms_office_version = forms.ChoiceField(choices=MS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    Email_Type = forms.ChoiceField(choices=Email_Type,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    ms_visio = forms.ChoiceField(choices=VISIO_VERSION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    ms_access = forms.ChoiceField(choices=ACCESS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    OEM_Volume = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Antivirus = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    AutoCAD = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Adobe_acrobate = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Visio = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    Access = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    SAP = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    SAP_User_ID = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Status = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}),required=False)

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
    Machine_Sl_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    Machine_Number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Purchase_Date = forms.DateField(label='Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Details = forms.DateField(label='Warranty End Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS,widget=forms.Select(attrs={'class': 'form-control'}))
    Devices = forms.ChoiceField(choices=DEVICES,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = WifiModel
        fields = '__all__'

class FirewallForm(forms.ModelForm):
    Location = forms.ChoiceField(choices=LOCATION, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    Old_Asst_No = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)
    Asst_No = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    User_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                       required=False)
    Machine_Sl_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    Machine_Number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     required=False)
    Purchase_Date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS, widget=forms.Select(attrs={'class': 'form-control'}))
    Machine_Type = forms.ChoiceField(choices=MACHINE_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = FirewallModel
        fields = '__all__'

class VCCForm(forms.ModelForm):
    Location = forms.ChoiceField(choices=LOCATION, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    Asst_No = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Machine_Type = forms.ChoiceField(choices=MACHINE_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
    Make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Machine_Model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                       required=False)
    Machine_Si_No = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=False)
    Purchased_Date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    Warranty_Exp_Date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_Start_Date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    AMC_End_Date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    Remarks = forms.ChoiceField(choices=REMARKS, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = VCCModel
        fields = '__all__'

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


'''('Cal','Cal'),
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
    ('Shredding','Shredding'),'''