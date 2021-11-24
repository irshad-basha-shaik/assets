
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AssetForm,WifiForm,FirewallForm
from .models import AssetModel,WifiModel,FirewallModel
# Create your views here.


def new(request):
    context = {}
    context['form'] = AssetForm()
    if request.method== 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return index(request)
    return render(request,"assets_entry.html",context)
def index(request):
    list = AssetModel.objects.all()
    return render(request,"assets.html",{"list":list})
def edit(request,id):
    obj = get_object_or_404(AssetModel, pk=id)
    context = {}
    form = AssetForm(instance=obj)
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            AssetModel.objects.filter(pk=id).update(user_name=form.cleaned_data['user_name'],location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],user_email=form.cleaned_data['user_email'], emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgroup=form.cleaned_data['domain_workgroup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'],processor=form.cleaned_data['processor'],processor_purchase_date=form.cleaned_data['processor_purchase_date'],warranty_start_date=form.cleaned_data['warranty_start_date'],warranty_end_date=form.cleaned_data['warranty_end_date'],amc_start_date=form.cleaned_data['amc_start_date'],amc_end_date=form.cleaned_data['amc_end_date'],user_acceptance_date=form.cleaned_data['user_acceptance_date'],user_handed_over_date=form.cleaned_data['user_handed_over_date'],ms_office=form.cleaned_data['ms_office'],ms_office_version=form.cleaned_data['ms_office_version'],OEM_Volume=form.cleaned_data['OEM_Volume'],Operating_System_Version=form.cleaned_data['Operating_System_Version'],OS=form.cleaned_data['OS'],Antivirus=form.cleaned_data['Antivirus'],AutoCAD=form.cleaned_data['AutoCAD'],Adobe_acrobate=form.cleaned_data['Adobe_acrobate'],Visio=form.cleaned_data['Visio'],Access=form.cleaned_data['Access'],SAP_User_ID=form.cleaned_data['SAP_User_ID'],SAP=form.cleaned_data['SAP'],Status=form.cleaned_data['Status'],Remarks=form.cleaned_data['Remarks'])

            return index(request)
    context['form'] = form
    return render(request,"assets_edit.html",context)
def delete(request,id):
    context = {}
    obj = get_object_or_404(AssetModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")


def wifi(request):
    context = {}
    context['form'] = WifiForm()
    if request.method == 'POST':
        form = WifiForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return wifi_index(request)
    return render(request, "wifi_entry.html", context)

def wifi_index(request):
    list = WifiModel.objects.all()
    return render(request, "wifi.html", {"list": list})

def wifi_edit(request,id):
    obj = get_object_or_404(WifiModel, pk=id)
    context = {}
    form = WifiForm(instance=obj)
    if request.method == 'POST':
        form = WifiForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            WifiModel.objects.filter(pk=id).update(Location=form.cleaned_data['Location'],Old_Asst_No=form.cleaned_data['Old_Asst_No'],Asst_No=form.cleaned_data['Asst_No'], User_name_Location=form.cleaned_data['User_name_Location'],Make=form.cleaned_data['Make'],Machine_Model_no=form.cleaned_data['Machine_Model_no'],Machine_Sl_no=form.cleaned_data['Machine_Sl_no'],Machine_Number=form.cleaned_data['Machine_Number'],Purchase_Date=form.cleaned_data['Purchase_Date'],Warranty_Details=form.cleaned_data['Warranty_Details'],AMC_Date=form.cleaned_data['AMC_Date'],Remarks=form.cleaned_data['Remarks'],Devices=form.cleaned_data['Devices'])

            return wifi_index(request)
    context['form'] = form
    return render(request,"wifi_edit.html",context)

def wifi_delete(request,id):
    context = {}
    obj = get_object_or_404(WifiModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")

def firewall(request):
    context = {}
    context['form'] = FirewallForm()
    if request.method == 'POST':
        form = FirewallForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return firewall_index(request)
    return render(request, "firewall_entry.html", context)

def firewall_index(request):
    list = FirewallModel.objects.all()
    return render(request, "firewall.html", {"list": list})

def firewall_edit(request,id):
    obj = get_object_or_404(WifiModel, pk=id)
    context = {}
    form = FirewallForm(instance=obj)
    if request.method == 'POST':
        form = FirewallForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            FirewallModel.objects.filter(pk=id).update(Location=form.cleaned_data['Location'],Old_Asst_No=form.cleaned_data['Old_Asst_No'],Asst_No=form.cleaned_data['Asst_No'], User_name_Location=form.cleaned_data['User_name_Location'],Make=form.cleaned_data['Make'],Machine_Model_no=form.cleaned_data['Machine_Model_no'],Machine_Sl_no=form.cleaned_data['Machine_Sl_no'],Machine_Number=form.cleaned_data['Machine_Number'],Purchase_Date=form.cleaned_data['Purchase_Date'],Warranty_Details=form.cleaned_data['Warranty_Details'],AMC_Date=form.cleaned_data['AMC_Date'],Remarks=form.cleaned_data['Remarks'],Devices=form.cleaned_data['Devices'])

            return firewall_index(request)
    context['form'] = form
    return render(request,"firewall_edit.html",context)

def firewall_delete(request,id):
    context = {}
    obj = get_object_or_404(FirewallModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")