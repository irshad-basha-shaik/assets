from datetime import datetime

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AssetForm,WifiForm,FirewallForm,VCCForm,PrintersForm,AVAILABLE_LICENCE,AVAILABLE_LICENCE_ORDER, LOCATION, OS, MS_VERSION
from .models import AssetModel,WifiModel,FirewallModel,VCCModel,PrinterModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse

@csrf_exempt

def new(request):
    context = {}
    context['form'] = AssetForm()
    if request.method== 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return index(request)
        else:
            print(form.errors)

    return render(request,"assets_entry.html",context)
def index(request):
    list = AssetModel.objects.all()
    return render(request,"assets.html",{"list":list})
def OSTally():
    win_live = []
    ser_live = []
    for os in OS:
        c1 = getAssetCount(os[1], False)
        c2 = getAssetCount(os[1], True)
        c3 = getAvailableLicence(os[1])
        c4 = c3 - c1
        c5 = False
        c6 = True
        if (c4 < 0):
            c5 = True
            c6 = False
        temp = {"OS": os[1], "VolumeLicence": c1, "OEM": c2, "pos": 0, "Available": c3, "Balance": c4,
                 "CurrentAvailableBalance": c4, "BorrowPath": []}
        if os[1].startswith("Win."):
            b = getOSPosition(os[1])
            temp['pos'] = b
            win_live.append(temp)
        elif os[1].startswith("Ser."):
            b = getOSPosition(os[1])
            temp['pos'] = b
            ser_live.append(temp)
    win_live = generateCarryForward(win_live)
    ser_live = generateCarryForward(ser_live)
    return win_live,ser_live
def MSOFfice():
    win_live = []
    ser_live = []
    for os in MS_VERSION:
        c1 = getMSOfficeCount(os[1])
        c3 = getAvailableLicence(os[1])
        c4 = c3 - c1
        c5 = False
        c6 = True
        if (c4 < 0):
            c5 = True
            c6 = False
        temp = {"OS": os[1], "VolumeLicence": c1,  "pos": 0, "Available": c3, "Balance": c4,
                 "CurrentAvailableBalance": c4, "BorrowPath": []}
        b = getOSPosition(os[1])
        temp['pos'] = b
        if temp["OS"]!='':
            win_live.append(temp)

    win_live = generateCarryForward(win_live)
    return win_live
def fetchBalance(need1,x,list):
    need=need1*-1
    for y in list:
        if x['pos']<y['pos']:
            if y['CurrentAvailableBalance'] >=need:
                temp = y['CurrentAvailableBalance'] - need
                y['CurrentAvailableBalance']=temp
                x['CurrentAvailableBalance'] = 0
                ttemp={"LenderVersion":y["OS"],"BorrowLicence":need}
                x["BorrowPath"].append(ttemp)
                return 0
            elif y['CurrentAvailableBalance'] >0:
                tal=y['CurrentAvailableBalance']
                need =  need -y['CurrentAvailableBalance']
                y['CurrentAvailableBalance'] = 0
                x['CurrentAvailableBalance'] = need*-1
                ttemp = {"LenderVersion": y["OS"], "BorrowLicence": tal}
                x["BorrowPath"].append(ttemp)
    return need
def generateCarryForward(list):
    for x in list:
        if x["Balance"]<0:
            need= x["Balance"]
            fetchBalance(need,x,list)
            i=10
    return list
def getOSPosition(obj):
    s= None
    try:
        s=AVAILABLE_LICENCE_ORDER[obj]
        if s!= None:
            return s
    except:
        return -1
def getAvailableLicence(obj):
    try:
        s=AVAILABLE_LICENCE[obj]
    except:
        s=-1

    return s
def getAssetCount(os,oem):
    list = AssetModel.objects.all().filter(OS=os,OEM_Volume=oem)
    return len(list)
def getMSOfficeCount(oem):
    list = AssetModel.objects.all().filter(ms_office_version=oem)
    return len(list)
def home(request):
    context = {}
    a,b=OSTally()
    now = datetime.today()
    context['win'] = a
    context['winSum'] = sum(a)
    context['server'] = b
    context['serverSum'] = sum(a)
    context['MSOFfice'] = MSOFfice()
    context['now'] = now

    return render(request, "home.html", context)
def sum(obj):
    temp = { "VolumeLicence":  0, "Available": 0, "Balance": 0,
            "CurrentAvailableBalance": 0}
    for  x in obj:
        temp["VolumeLicence"]=temp["VolumeLicence"]+x["VolumeLicence"]
        temp["Available"] = temp["Available"] + x["Available"]
        temp["Balance"] = temp["Balance"] + x["Balance"]
        temp["CurrentAvailableBalance"] = temp["CurrentAvailableBalance"] + x["CurrentAvailableBalance"]
    return temp
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

def vcc(request):
    context = {}
    context['form'] = VCCForm()
    if request.method == 'POST':
        form = VCCForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return vcc_index(request)
    return render(request, "vcc_entry.html", context)

def vcc_index(request):
    list = VCCModel.objects.all()
    return render(request, "vcc.html", {"list": list})

def vcc_edit(request,id):
    obj = get_object_or_404(VCCModel, pk=id)
    context = {}
    form = VCCForm(instance=obj)
    if request.method == 'POST':
        form = VCCForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            VCCModel.objects.filter(pk=id).update(Location=form.cleaned_data['Location'],Old_Asst_No=form.cleaned_data['Old_Asst_No'],Asst_No=form.cleaned_data['Asst_No'], User_name_Location=form.cleaned_data['User_name_Location'],Make=form.cleaned_data['Make'],Machine_Model_no=form.cleaned_data['Machine_Model_no'],Machine_Sl_no=form.cleaned_data['Machine_Sl_no'],Machine_Number=form.cleaned_data['Machine_Number'],Purchase_Date=form.cleaned_data['Purchase_Date'],Warranty_Details=form.cleaned_data['Warranty_Details'],AMC_Date=form.cleaned_data['AMC_Date'],Remarks=form.cleaned_data['Remarks'],Devices=form.cleaned_data['Devices'])

            return vcc_index(request)
    context['form'] = form
    return render(request,"vcc_edit.html",context)

def vcc_delete(request,id):
    context = {}
    obj = get_object_or_404(VCCModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")


def printer(request):
    context = {}
    context['form'] = PrintersForm()
    if request.method == 'POST':
        form = PrintersForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return printer_index(request)
    return render(request, "printer_entry.html", context)

def printer_index(request):
    list = PrinterModel.objects.all()
    return render(request, "printer.html", {"list": list})

def printer_edit(request,id):
    obj = get_object_or_404(PrinterModel, pk=id)
    context = {}
    form = PrintersForm(instance=obj)
    if request.method == 'POST':
        form = PrintersForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            PrinterModel.objects.filter(pk=id).update(Location=form.cleaned_data['Location'],Old_Asst_No=form.cleaned_data['Old_Asst_No'],Asst_No=form.cleaned_data['Asst_No'], User_name_Location=form.cleaned_data['User_name_Location'],Make=form.cleaned_data['Make'],Machine_Model_no=form.cleaned_data['Machine_Model_no'],Machine_Sl_no=form.cleaned_data['Machine_Sl_no'],Machine_Number=form.cleaned_data['Machine_Number'],Purchase_Date=form.cleaned_data['Purchase_Date'],Warranty_Details=form.cleaned_data['Warranty_Details'],AMC_Date=form.cleaned_data['AMC_Date'],Remarks=form.cleaned_data['Remarks'],Devices=form.cleaned_data['Devices'])

            return vcc_index(request)
    context['form'] = form
    return render(request,"printer_edit.html",context)

def printer_delete(request,id):
    context = {}
    obj = get_object_or_404(PrinterModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")