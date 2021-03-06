from datetime import datetime,date
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AssetForm,WifiForm,FirewallForm,VCCForm,PrintersForm,AVAILABLE_LICENCE,AVAILABLE_LICENCE_ORDER, LOCATION, OS, MS_VERSION, REMARKS, MACHINE_TYPE,USAGE_TYPE,EmailType
from .models import AssetModel,WifiModel,FirewallModel,VCCModel,PrinterModel
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
log=""


@csrf_exempt

@login_required
def new(request):
    context = {}
    context['form'] = AssetForm()
    if request.method== 'POST':

        form = AssetForm(request.POST)
        #form = form.upper()
        if form.is_valid():
            student = form.save(commit=False)
            #a = form.cleaned_data['processor_purchase_date']
            """student.machine_age = getMachineAge(form.cleaned_data['processor_purchase_date'])
            student.email_type=form.cleaned_data['ms_365']
            student.Installed_Softwares = form.cleaned_data['Installed_Softwares']"""
            student.save()
            return index(request)
        else:
            print("---error---start---")
            print(request.POST)
            print(form.errors)
            print("---error---end---")

    return render(request,"assets_entry.html",context)
def it_assets(request):
    list = getAssets()
    list4 = getAssetsByLocation()
    list['vol']= list4
    list5 = getAssetsByLocationAntivirus()
    list['antivirus'] = list5
    list6 = getAssetsByLocationDomain()
    list['cal'] = list6
    list7 = getAssetsByLocationMs365()
    list['O365'] = list7
    if request.content_type == 'application/json':
        return JsonResponse(list)
    return render(request, "it_assets.html", list)
def getMachineAge(purchasedate):
    days_in_year = 365.2425
    age = int((date.today() - purchasedate).days / days_in_year)
    return age

def getAssetsByLocationMs365():
    list = {"location": [], "data": []}
    r = "MS Office 365"
    total = 0
    for l1 in range(len(LOCATION)):
        l = LOCATION[l1]
        dat = getAssetCountByLocationO365(l[1], r)
        total = total + dat
        list['location'].append({"LOCATION": l[1], "data": dat})
    list['location'].append({"Total": total})
    return list
def getAssetsByLocationDomain():
    list = {"location": [], "data": []}
    r = "Domain / Workgoup"
    total = 0
    for l1 in range(len(LOCATION)):
        l = LOCATION[l1]
        dat = getAssetCountByLocationDomain(l[1], r)
        total = total + dat
        list['location'].append({"LOCATION": l[1], "data": dat})
    list['location'].append({"Total": total})
    return list


def getAssetCountByLocationDomain(l, r):
    if r == 'Domain / Workgoup':
        list = AssetModel.objects.all().filter(domain_workgroup='Domain', location=l)
    return len(list)

def getAssetsByLocationAntivirus():
    list = { "location": [],"data": []}
    r = "Antivirus"
    total = 0
    for l1 in range(len(LOCATION)):
        l = LOCATION[l1]
        dat = getAssetCountByLocationAntivirus(l[1], r)
        total = total+dat
        list['location'].append({"LOCATION": l[1], "data": dat})
    list['location'].append({"Total": total})
    return list
def getAssetCountByLocationAntivirus(l,r):
    r1 = False
    if r == 'Antivirus':
        r1 = True
        list = AssetModel.objects.all().filter(Antivirus=r1, location=l)
    return len(list)
def getAssetsByLocation():
    list = {"remark":[],"LOCATION":LOCATION,"gtotal":[]}
    REM = [("OS Windows Details (Volume)", ["Win.XP", "Win.7", "Win.8", "Win.10", "Win.11"], 6, "Total"),
           ("OS Server Details (Volume)", ["Ser.2012", "Ser.2016", "Ser.2019"], 4, "Total"),
           ("OS Details (OEM)", ["Win.7", "Win.8", "Win.10", "Win.11"], 5, "Total"),
            ("MS Office Details",["MS Office Standard 2010", "MS Office Standard 2013", "MS Office Standard 2016", "MS Office Standard 2019"], 5, "Total")]

    grand_total = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(REM)):
        r=REM[i][0]
        MTYP=REM[i][1]
        TTYPE=REM[i][3]
        list1 ={"name":"","machine":[],"SUBCOUNT":(REM[i][2]) }
        list1["name"] = r
        total = [0, 0, 0, 0, 0, 0, 0]
        gct = 0
        for mtypes in MTYP:
            list2 ={"name":"Total","location":[],"ALLLocationSUM":0 }
            list2["name"] = mtypes

           # list2["ALLLocationSUM"] = mtypes
            for l1 in  range(len(LOCATION)):
                l= LOCATION[l1]
                dat = getAssetCountByLocationRemarksOS(l[1],r,mtypes)
                list2['location'].append({"LOCATION": l[1],"Machine": mtypes[1],"remark":r[1],"data":dat})
                td = total[l1]
                td = td+dat
                total[l1]=td
                tdd = grand_total[l1]
                tdd=tdd+dat
                grand_total[l1]=tdd
                ltd = list2["ALLLocationSUM"]
                ltd = ltd + dat
                list2["ALLLocationSUM"] = ltd
            list1['machine'].append(list2)
        gltt=0
        tot={"name":TTYPE,"location":[]}
        list['remark'].append(list1)
        for x in range(len(list1['machine'][0]['location'])):
            tot['location'].append({"name":"total","data":total[x]})
        gct=0
        for x in tot['location']:
            gct = gct + x['data']
        tot['location'].append({"name": "typetotaltotal", "data": gct})
        list1['machine'].append(tot)
    ggct = 0
    for x in grand_total:
        ggct = ggct + x
    grand_total.append(ggct)
    list["gtotal"]=grand_total
    return list
def getAssets():
    list = {"remark":[],"LOCATION":LOCATION,"gtotal":[]}
    REM = [ ("Used Workstations",["Desktop","Laptop", "Server"],4,"Total Used") ,
            ("Spare_Old Workstations",["Desktop","Laptop"],3,"Total Old Spare"),
            ("Spare_New  Workstations",["Desktop","Laptop"],3,"Total New spare")]
    grand_total = [0, 0, 0, 0, 0, 0]
    for i in range(len(REM)):
        r=REM[i][0]
        MTYP=REM[i][1]
        TTYPE=REM[i][3]
        list1 ={"name":"","machine":[],"SUBCOUNT":(REM[i][2]) }
        list1["name"] = r
        total = [0, 0, 0, 0, 0, 0]
        gct = 0
        for mtypes in MTYP:
            list2 ={"name":"Total","location":[],"ALLLocationSUM":0 }
            list2["name"] = mtypes

           # list2["ALLLocationSUM"] = mtypes
            for l1 in  range(len(LOCATION)):
                l= LOCATION[l1]
                dat = getAssetCountByLocationRemarksMachineType(l[1],r,mtypes)
                list2['location'].append({"LOCATION": l[1],"Machine": mtypes[1],"remark":r[1],"data":dat})
                td = total[l1]
                td = td+dat
                total[l1]=td
                tdd = grand_total[l1]
                tdd=tdd+dat
                grand_total[l1]=tdd
                ltd = list2["ALLLocationSUM"]
                ltd = ltd + dat
                list2["ALLLocationSUM"] = ltd
            list1['machine'].append(list2)
        gltt=0
        tot={"name":TTYPE,"location":[]}
        list['remark'].append(list1)
        for x in range(len(list1['machine'][0]['location'])):
            tot['location'].append({"name":"total","data":total[x]})
        gct=0
        for x in tot['location']:
            gct = gct + x['data']
        tot['location'].append({"name": "typetotaltotal", "data": gct})
        list1['machine'].append(tot)
    ggct = 0
    for x in grand_total:
        ggct = ggct + x
    grand_total.append(ggct)
    list["gtotal"]=grand_total
    return list

def index(request):
    list = AssetModel.objects.all()
    if request.content_type == 'application/json':
        return JsonResponse(list)
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
    for os in MS_VERSION:
        c1 = getMSOfficeCount(os[1])
        c3 = getAvailableLicence(os[1])
        c4 = c3 - c1
        c5 = False
        c6 = True
        if (c4 < 0):
            c5 = True
            c6 = False
        temp = {"OS": os[1], "VolumeLicence": c1, "OEM": 0, "pos": 0, "Available": c3, "Balance": c4,
                 "CurrentAvailableBalance": c4, "BorrowPath": []}
        b = getOSPosition(os[1])
        temp['pos'] = b
        if temp["OS"]!='':
            win_live.append(temp)

    win_live = generateCarryForward(win_live)
    return win_live

def MS365():
    MS365 = []
    Zimbra = []
    for os in EmailType:
        c1 = getMS365Count(os[1])
        c2 = getAssetCount(os[1], True)
        c3 = getAvailableLicence(os[1])
        c4 = c3 - c1
        c5 = False
        c6 = True
        if (c4 < 0):
            c5 = True
            c6 = False
        temp = {"O365": os[1], "VolumeLicence": c1, "OEM": c2, "pos": 0, "Available": c3, "Balance": c4,
                "CurrentAvailableBalance": c4, "BorrowPath": []}
        if os[1].startswith("MS Office 365"):
            b = getOSPosition(os[1])
            temp['pos'] = b
            MS365.append(temp)
        if os[1].startswith("Zimbra"):
            b = getOSPosition(os[1])
            temp['pos'] = b
            Zimbra.append(temp)

    MS365 = generateCarryForward(MS365)
    Zimbra = generateCarryForward(Zimbra)


    return MS365,Zimbra
def Zimbra():
    MS365 = []
    for os in EmailType:
        c1 = getMS365Count(os[1])
        c2 = getAssetCount(os[1], True)
        c3 = getAvailableLicence(os[1])
        c4 = c3 - c1
        c5 = False
        c6 = True
        if (c4 < 0):
            c5 = True
            c6 = False
        temp = {"O365": os[1], "VolumeLicence": c1, "OEM": c2, "pos": 0, "Available": c3, "Balance": c4,
                "CurrentAvailableBalance": c4, "BorrowPath": []}
        if os[1].startswith("MS Office 365"):
            b = getOSPosition(os[1])
            temp['pos'] = b
            MS365.append(temp)

    MS365 = generateCarryForward(MS365)

    return MS365
def CALDomain():
    CAL = []
    os = 'Domain'
    c1 = getCALCount(os)
    c3 = getAvailableLicence(os)
    c4 = c3 - c1
    c5 = False
    c6 = True
    if (c4 < 0):
        c5 = True
        c6 = False
    temp = {"CAL": os, "VolumeLicence": c1, "OEM": 0, "pos": 0, "Available": c3, "Balance": c4,
            "CurrentAvailableBalance": c4, "BorrowPath": []}
    if os.startswith("Domain"):
        b = getOSPosition(os)
        temp['pos'] = b
        CAL.append(temp)

    CAL = generateCarryForward(CAL)

    return CAL

def Antivirus():
    Anti = []
    os = 'Antivirus'
    c1 = getAntivirusCount(os)
    c3 = getAvailableLicence(os)
    c4 = c3 - c1
    c5 = False
    c6 = True
    if (c4 < 0):
        c5 = True
        c6 = False
    temp = {"Anti": os, "VolumeLicence": c1, "OEM": 0, "pos": 0, "Available": c3, "Balance": c4,
            "CurrentAvailableBalance": c4, "BorrowPath": []}
    if os.startswith("Antivirus"):
        b = getOSPosition(os)
        temp['pos'] = b
        Anti.append(temp)

    Anti = generateCarryForward(Anti)
    return Anti
def getAntivirusCount(os):
    list = AssetModel.objects.all().filter(Antivirus='True')
    return len(list)
def fetchBalance(need1,x,list):
    need=need1*-1
    for y in list:
        if x['pos']<y['pos']:
            if y['Available'] >=need:
                temp = y['CurrentAvailableBalance'] - need
                y['CurrentAvailableBalance']=temp
                x['CurrentAvailableBalance'] = 0
                ttemp={"LenderVersion":y["OS"],"BorrowLicence":need}
                x["BorrowPath"].append(ttemp)
                return 0
            elif y['Available'] < need:
                #tal=y['CurrentAvailableBalance']
                need2 =  need -y['CurrentAvailableBalance']
                k=y['CurrentAvailableBalance']
                ttemp = {"LenderVersion": y["OS"], "BorrowLicence": k}
                y['CurrentAvailableBalance'] = 0
                x['CurrentAvailableBalance'] = need2*-1

                x["BorrowPath"].append(ttemp)
    return need
def generateCarryForward(list):
    for x in list:
        if x['CurrentAvailableBalance']<0:
            need= x["CurrentAvailableBalance"]
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
def getAssetCountByLocationRemarksMachineType(l,r,m):

    if r == 'Used Workstations' :
        list = AssetModel.objects.all().filter(usage_type='Live', machine_type=m, location=l)
    elif r == 'Spare_Old Workstations' :
        list = AssetModel.objects.all().filter(user_name__iexact='Spare Old',machine_type=m, location=l).exclude(Status='Not working')
    elif r == 'Spare_New  Workstations' :
        list = AssetModel.objects.all().filter(user_name__iexact='Spare New',machine_type=m, location=l).exclude(Status='Not working')
    return len(list)

def getAssetCountByLocationRemarksOS(l,r,m):
    r1= False
    if r=='OS Windows Details (Volume)':
        r1 = False
        list = AssetModel.objects.all().filter(OEM_Volume=r1, OS=m, location=l).exclude(user_name__iexact='Spare')
    elif r == 'OS Server Details (Volume)':
        r1 = False
        list = AssetModel.objects.all().filter(OEM_Volume=r1, OS=m, location=l).exclude(user_name__iexact='Spare')
    elif r == 'OS Details (OEM)':
        r1 = True
        list = AssetModel.objects.all().filter(OEM_Volume=r1, OS=m, location=l).exclude(user_name__iexact='Spare Old')
    else:
        r1 = True
        list = AssetModel.objects.all().filter(ms_office=r1, ms_office_version=m, location=l)
    return len(list)
def getAssetCountByLocationO365(l,r):
    if r=='MS Office 365':
        list = AssetModel.objects.all().filter(ms_365=r, location=l)
    return len(list)
def getAssetCount(os,oem):
    list = AssetModel.objects.all().filter(OS=os,OEM_Volume=oem,usage_type='Live')
    return len(list)

def getMSOfficeCount(oem):
    list = AssetModel.objects.all().filter(ms_office_version=oem,usage_type='Live')
    return len(list)
def getCALCount(domain_workgroup):
    list = AssetModel.objects.all().filter(domain_workgroup='Domain')
    return len(list)
def getMS365Count(oem):
    list = AssetModel.objects.all().filter(ms_365=oem)
    return len(list)
def home(request):
    context = {}
    a,b=OSTally()
    now = datetime.today()
    context['win'] = a
    context['winSum'] = sum(a)
    context['server'] = b
    context['serverVolumeSum'] = sum(b)
    c = MSOFfice()
    context['MSOFfice'] = c
    context['MSOFficeSum'] = sum(c)
    d = MS365()
    context['MS365'] = d[0]
    context['MS365Sum'] = sum(d[0])
    context['Zimbra'] = d[1]
    context['ZimbraSum'] = sum(d[1])
    e = CALDomain()
    context['CAL'] = e
    context['CALSum'] = sum(e)
    f = Antivirus()
    context['Antivirus'] = f
    context['AntivirusSum'] = sum(f)
    context['now'] = now
    if request.content_type == 'application/json':
        return JsonResponse(context)
    return render(request, "home.html", context)
def sum(obj):
    temp = { "VolumeLicence":  0, "OEM": 0,"Available": 0, "Balance": 0,
            "CurrentAvailableBalance": 0}
    for  x in obj:
        temp["VolumeLicence"]=temp["VolumeLicence"]+x["VolumeLicence"]
        temp["Available"] = temp["Available"] + x["Available"]
        temp["OEM"] = temp["OEM"] + x["OEM"]
        temp["Balance"] = temp["Balance"] + x["Balance"]
        temp["CurrentAvailableBalance"] = temp["CurrentAvailableBalance"] + x["CurrentAvailableBalance"]
    return temp
@login_required
def edit(request,id):
    obj = get_object_or_404(AssetModel, pk=id)
    context = {}
    form = AssetForm(instance=obj)
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            AssetModel.objects.filter(pk=id).update(user_name=form.cleaned_data['user_name'],user_contact=form.cleaned_data['user_contact'],location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],user_email=form.cleaned_data['user_email'], emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],machine_age=form.cleaned_data['machine_age'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgroup=form.cleaned_data['domain_workgroup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'],processor=form.cleaned_data['processor'],processor_purchase_date=form.cleaned_data['processor_purchase_date'],warranty_start_date=form.cleaned_data['warranty_start_date'],warranty_end_date=form.cleaned_data['warranty_end_date'],amc_start_date=form.cleaned_data['amc_start_date'],amc_end_date=form.cleaned_data['amc_end_date'],user_acceptance_date=form.cleaned_data['user_acceptance_date'],user_handed_over_date=form.cleaned_data['user_handed_over_date'],ms_office=form.cleaned_data['ms_office'],ms_office_version=form.cleaned_data['ms_office_version'],OEM_Volume=form.cleaned_data['OEM_Volume'],Operating_System_Version=form.cleaned_data['Operating_System_Version'],OS=form.cleaned_data['OS'],Antivirus=form.cleaned_data['Antivirus'],AutoCAD=form.cleaned_data['AutoCAD'],Adobe_acrobate=form.cleaned_data['Adobe_acrobate'],Visio=form.cleaned_data['Visio'],Access=form.cleaned_data['Access'],ms_visio=form.cleaned_data['ms_visio'],ms_access=form.cleaned_data['ms_access'],SAP_User_ID=form.cleaned_data['SAP_User_ID'],SAP=form.cleaned_data['SAP'],ms_365=form.cleaned_data['ms_365'],Installed_Softwares=form.cleaned_data['Installed_Softwares'], Status=form.cleaned_data['Status'],Remarks=form.cleaned_data['Remarks'])
            return index(request)
    context['form'] = form
    return render(request,"assets_edit.html",context)
@login_required
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