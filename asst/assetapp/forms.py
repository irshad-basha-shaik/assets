from django import forms


from django import forms



# creating a form
from .models import AssetModel

USAGE_TYPE = [
    ('Spare_Old', 'Spare_Old'),
    ('Spare_New', 'Spare_New')
]
LOCATION = [
    ('Hyd', 'Hyd'),
    ('Cht', 'Cht'),
    ('Kdp', 'Kdp'),
    ('Wg', 'Wg'),
    ('Eg', 'Eg'),
    ('Warangal', 'Warangal'),
]
MACHINE_TYPE = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
]
HDD = [
    ('120GB', '120GB'),
    ('240GB', '240GB'),
    ('500GB', '500GB'),
    ('1000GB', '1000GB'),
    ('2000GB', '2000GB'),
    ('10000GB', '10000GB'),
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
OS_VERSION = [x for x in range(1990,2021)]
MS_VERSION = [x for x in range(1990,2021)]
OEM_VOLUME = [x for x in range(1990,2021)]
OS = [
    ('Windows 1.01','Windows 1.01'),
    ('Windows 1.02','Windows 1.02'),
    ('Windows 1.03','Windows 1.03'),
    ('Windows 1.04','Windows 1.04'),
    ('Windows 2.01','Windows 2.01'),
    ('Windows 2.03','Windows 2.03'),
    ('Windows 2.1','Windows 2.1'),
    ('Windows 2.11','Windows 2.11'),
    ('Windows 3.0','Windows 3.0'),
    ('Windows 3.1','Windows 3.1'),
    ('Windows NT 3.1','Windows NT 3.1'),
    ('Windows 3.11','Windows 3.11'),
    ('Windows 3.2','Windows 3.2'),
    ('Windows NT 3.5','Windows NT 3.5'),
    ('Windows NT 3.51','Windows NT 3.51'),
    ('Windows 95','Windows 95'),
    ('Windows NT 4.0','Windows NT 4.0'),
    ('Windows 98','Windows 98'),
    ('Windows 98 Second Edition','Windows 98 Second Edition'),
    ('Windows 2000','Windows 2000'),
    ('Windows Me','Windows Me'),
    ('Windows XP','Windows XP'),
    ('Windows Vista','Windows Vista'),
    ('Windows 7','Windows 7'),
    ('Windows 8','Windows 8'),
    ('Windows 8.1','Windows 8.1'),
    ('Windows 10 version 1507','Windows 10 version 1507'),
    ('Windows 10 version 1511','Windows 10 version 1511'),
    ('Windows 10 version 1607','Windows 10 version 1607'),
    ('Windows 10 version 1703','Windows 10 version 1703'),
    ('Windows 10 version 1709','Windows 10 version 1709'),
    ('Windows 10 version 1803','Windows 10 version 1803'),
    ('Windows 10 version 1809','Windows 10 version 1809'),
    ('Windows 10 version 1903','Windows 10 version 1903'),
    ('Windows 10 version 1909','Windows 10 version 1909'),
    ('Windows 10 version 2004','Windows 10 version 2004'),
    ('Windows 10 version 20H2','Windows 10 version 20H2'),
    ('Windows 10 version 21H1','Windows 10 version 21H1'),
    ('Windows 10 version 21H2','Windows 10 version 21H2'),
    ('Windows 11 version 21H2','Windows 11 version 21H2'),
]
class AssetForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION,widget=forms.Select(attrs={'class': 'form-control'}))
    asset_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    emp_id = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    usage_type = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=USAGE_TYPE))
    machine_type = forms.ChoiceField(choices=MACHINE_TYPE,widget=forms.Select(attrs={'class': 'form-control'}))
    gef_id_number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    domain_workgoup = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_make = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_model_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    machine_serial_no = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd = forms.ChoiceField(choices=HDD,widget=forms.Select(attrs={'class': 'form-control'}))
    hdd_make = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd_model = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    hdd_serial_no =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    processor_purchase_date = forms.DateField(label='Processor Purchase Date', widget=forms.SelectDateWidget(years=YEARS))
    processor = forms.ChoiceField(choices=PROCESSOR,widget=forms.Select(attrs={'class': 'form-control'}))
    warranty_start_date = forms.DateField(label='Warranty Start Date', widget=forms.SelectDateWidget(years=YEARS))
    warranty_end_date = forms.DateField(label='Warranty End Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_start_date = forms.DateField(label='AMC Start Date', widget=forms.SelectDateWidget(years=YEARS))
    amc_end_date = forms.DateField(label='AMC End Date', widget=forms.SelectDateWidget(years=YEARS))
    user_acceptance_date = forms.DateField(label='User Acceptance Date', widget=forms.SelectDateWidget(years=YEARS))
    user_handed_over_date = forms.DateField(label='User Handed Over Date', widget=forms.SelectDateWidget(years=YEARS))
    OS_Version = forms.ChoiceField(choices=OS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}))
    OS = forms.ChoiceField(choices=OS,widget=forms.Select(attrs={'class': 'form-control'}))
    #ms_office = forms.CharField(widget=forms.CheckboxInput,required=False)
    ms_office_version = forms.ChoiceField(choices=MS_VERSION,widget=forms.Select(attrs={'class': 'form-control'}))
    OEM_Volume = forms.ChoiceField(choices=OEM_VOLUME,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = AssetModel
        fields = ['location','asset_no','emp_id','usage_type','machine_type','gef_id_number','domain_workgoup','machine_make','machine_model_no','machine_serial_no','hdd','hdd_make','hdd_model','hdd_serial_no','ram','processor','processor_purchase_date','warranty_start_date','warranty_end_date','amc_start_date','amc_end_date','user_acceptance_date','user_handed_over_date']