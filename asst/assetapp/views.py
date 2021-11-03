from django.shortcuts import render
from .models import Assets_types,Assets,Ops,Acategory,Astatus,Location,Software

# Create your views here.

info1 = Assets.objects.all()
info2 = Assets_types.objects.all()
info4 = Astatus.objects.all()
info3 = Acategory.objects.all()
info5 = Location.objects.all()
info6 = Ops.objects.all()
info7 = Software.objects.all()
info = [info1,info2,info3,info4,info5,info6,info7]
def assets(request):
    a = Assets.objects.all()
    return render(request, "assets.html", {"alist": a})
def assets_entry(request):
    at = Assets_types.objects.all()
    a = Assets.objects.all()
    astatus= Astatus.objects.all()
    ac = Acategory.objects.all()
    al = Location.objects.all()
    aos = Ops.objects.all()
    asoft = Software.objects.all()

    return render(request,"assets_entry.html",{"atList":at,"alist":a,"aslist":astatus,"aclist":ac,"llist":al,"oslist":aos,"slist":asoft})
def asaveform(request):
    info = Assets.objects.all()
    if request.method == 'POST':

        form = Assets(location=request.POST['location'], asset_no=request.POST['asset_no'],serial_no=request.POST['serial_no'],emp_id=request.POST['emp_id'], user_name=request.POST['user_name'],usage_type=request.POST['usage_type'],gef_identification_number=request.POST['gef_identification_number'],machine_type=request.POST['machine_type'],
                          domain_workgoup=request.POST['domain_workgoup'], make=request.POST['make'],machine_model_no=request.POST['machine_model_no'],os_version=request.POST['version'], os=request.POST['osname'],antivirus=request.POST.get('antivirus',''),autocad=request.POST.get('autocad',''),adobe_acrobate=request.POST.get('adobe_acrobate',''),visio=request.POST.get('visio',''),access=request.POST.get('access',''),sap=request.POST.get('sap',''),
                          ms_office_version=request.POST['ms_office_version'],serial_no1=request.POST['serial_no1'],warranty_start_date=request.POST['warranty_start_date'],warranty_end_date=request.POST['warranty_end_date'],amc_start_date=request.POST['amc_start_date'], amc_end_date=request.POST['amc_end_date'],hdd=request.POST['hdd'], make1=request.POST['make1'],
                          ram=request.POST['ram'],processor=request.POST['processor'],purchase_date=request.POST['purchase_date'],user_acceptance_date=request.POST['user_acceptance_date'],user_handed_over_date=request.POST['user_handed_over_date'])
        form.save()
    if request.method == 'GET':
        return render(request, "assets.html", {"form_list": info})

    return render(request, "assets.html",
                  {"alist": info, "atList": info2, "aslist": info4, "aclist": info3, "llist": info5,
                   "oslist": info6, "slist": info7})


def editform(request):
    info = Assets.objects.all()
    d = Assets.objects.filter(id=request.POST['id']).update(location=request.POST['location'], asset_no=request.POST['asset_no'],serial_no=request.POST['serial_no'],emp_id=request.POST['emp_id'], user_name=request.POST['user_name'],usage_type=request.POST['usage_type'],gef_identification_number=request.POST['gef_identification_number'],machine_type=request.POST['machine_type'],
                          domain_workgoup=request.POST['domain_workgoup'], make=request.POST['make'],machine_model_no=request.POST['machine_model_no'],os_version=request.POST['version'], os=request.POST['osname'],antivirus=request.POST['antivirus'],autocad=request.POST['autocad'],adobe_acrobate=request.POST['adobe_acrobate'],visio=request.POST['visio'],access=request.POST['access'],sap=request.POST['sap'],
                          ms_office_version=request.POST['ms_office_version'],serial_no1=request.POST['serial_no1'],warranty_start_date=request.POST['warranty_start_date'],warranty_end_date=request.POST['warranty_end_date'],amc_start_date=request.POST['amc_start_date'], amc_end_date=request.POST['amc_end_date'],hdd=request.POST['hdd'], make1=request.POST['make1'],
                          ram=request.POST['ram'],processor=request.POST['processor'],purchase_date=request.POST['purchase_date'],user_acceptance_date=request.POST['user_acceptance_date'],user_handed_over_date=request.POST['user_handed_over_date'])

    return render(request, "assets.html", {"alist": info})
    #return render(request,"aeditform.html",{})
def a_edit(request):
    id = request.GET['id']
    form = Assets.objects.get(id=id)
    return render(request, "a_edit.html", {"form": form,"alist": info1, "atList": info2, "aslist": info4, "aclist": info3, "llist": info5,
                   "oslist": info6, "slist": info7})
def adelete(request):
    info = Assets.objects.all()
    d = Assets.objects.filter(id=request.GET['id']).delete()
    return render(request, "assets.html", {"alist": info,"atList":info2,"aslist":info4,"aclist":info3,"llist":info5,"oslist":info6,"slist":info7})




def assets_types(request):
    at=Assets_types.objects.all()
    return render(request,"asset_types.html",{"atList":at})
def atype_entry(request):
    return render(request,"atype_entry.html",{})
def asset_type_saveform(request):
    info=Assets_types.objects.all()
    form=Assets_types(dname=request.POST['dname'],code=request.POST['code'])
    form.save()
    return render(request,"asset_types.html",{"atList":info})
def atype_edit(request):
    id=request.GET['id']
    form=Assets_types.objects.get(id=id)
    return render(request,"atype_edit.html",{"form":form})
def atype_editform(request):
    info = Assets_types.objects.all()
    d = Assets_types.objects.filter(id=request.POST['id']).update(dname=request.POST['dname'],code=request.POST['code'])
    return render(request,"asset_types.html",{"atList":info})
def atype_delete(request):
    info = Assets_types.objects.all()
    d = Assets_types.objects.filter(id=request.GET['id']).delete()
    return render(request,"asset_types.html",{"atList":info})

def ops(request):
    d=Ops.objects.all()
    return render(request,"ops.html",{"oslist":d})
def ops_entry(request):
    return render(request,"ops_entry.html",{})
def ops_saveform(request):
    d=Ops.objects.all()
    form=Ops(osname=request.POST['osname'],version=request.POST['version'],licence=request.POST['licence'],iso=request.POST['iso'],ms_office_version=request.POST['ms_office_version'])
    form.save()
    return render(request,"ops.html",{"oslist":d})
def ops_edit(request):
    id=request.GET['id']
    form=Ops.objects.get(id=id)
    return render(request,"ops_edit.html",{"form":form})
def ops_editform(request):
    info =Ops.objects.all()
    d = Ops.objects.filter(id=request.POST['id']).update(osname=request.POST['osname'],version=request.POST['version'],licence=request.POST['licence'],iso=request.POST['iso'])
    return render(request,"ops.html",{"oslist":info})
def ops_delete(request):
    info = Ops.objects.all()
    d = Ops.objects.filter(id=request.GET['id']).delete()
    return render(request,"ops.html",{"oslist":info})



def acategory(request):
    info = Acategory.objects.all()
    return render(request,"acategory.html",{"aclist": info})
def acategory_entry(request):
    return render(request,"acategory_entry.html",{})
def acategory_saveform(request):
    info = Acategory.objects.all()
    form = Acategory(acname=request.POST['acname'])
    form.save()
    return render(request,"acategory.html",{"aclist":info})
def acategory_edit(request):
    id = request.GET['id']
    form = Acategory.objects.get(id=id)
    return render(request,"acategory_edit.html",{"form": form})
def acategory_editform(request):
    info = Acategory.objects.all()
    d = Acategory.objects.filter(id=request.POST['id']).update(acname=request.POST['acname'])
    return render(request,"acategory.html",{"aclist": info})
def acategory_delete(request):
    info = Acategory.objects.all()
    d = Acategory.objects.filter(id=request.GET['id']).delete()
    return render(request,"acategory.html",{"aclist": info})





def astatus(request):
    d = Astatus.objects.all()
    return render(request,"astatus.html",{"aslist": d})
def astatus_entry(request):
    return render(request,"astatus_entry.html",{})
def astatus_saveform(request):
    d = Astatus.objects.all()
    form = Astatus(asname=request.POST['asname'])
    form.save()
    return render(request,"astatus.html",{"aslist":d})
def astatus_edit(request):
    id = request.GET['id']
    form = Astatus.objects.get(id=id)
    return render(request,"astatus_edit.html",{"form": form})
def astatus_editform(request):
    info = Astatus.objects.all()
    d = Astatus.objects.filter(id=request.POST['id']).update(asname=request.POST['asname'])
    return render(request,"astatus.html",{"aslist": info})
def astatus_delete(request):
    info = Astatus.objects.all()
    d = Astatus.objects.filter(id=request.GET['id']).delete()
    return render(request,"astatus.html",{"aslist": info})



def location(request):
    d=Location.objects.all()
    return render(request,"location.html",{"llist":d})
def location_entry(request):
    return render(request,"location_entry.html",{})
def location_saveform(request):
    d=Location.objects.all()
    form=Location(name=request.POST['name'],adress=request.POST['adress'],owner=request.POST['owner'])
    form.save()
    return render(request,"location.html",{"llist":d})
def location_edit(request):
    id=request.GET['id']
    form=Location.objects.get(id=id)
    return render(request,"location_edit.html",{"form":form})
def location_editform(request):
    info = Location.objects.all()
    d = Location.objects.filter(id=request.POST['id']).update(name=request.POST['name'],adress=request.POST['adress'],owner=request.POST['owner'])
    return render(request,"location.html",{"llist":info})
def location_delete(request):
    info = Location.objects.all()
    d = Location.objects.filter(id=request.GET['id']).delete()
    return render(request,"location.html",{"llist":info})


def software(request):
    d=Software.objects.all()
    return render(request,"software.html",{"slist":d})
def software_entry(request):
    return render(request,"software_entry.html",{})
def software_saveform(request):
    d=Software.objects.all()
    form=Software(name=request.POST['name'],version=request.POST['version'],licence=request.POST['licence'])
    form.save()
    return render(request,"software.html",{"slist":d})
def software_edit(request):
    id=request.GET['id']
    form=Software.objects.get(id=id)
    return render(request,"software_edit.html",{"form":form})
def software_editform(request):
    info = Software.objects.all()
    d = Software.objects.filter(id=request.POST['id']).update(name=request.POST['name'],version=request.POST['version'],licence=request.POST['licence'])
    return render(request,"software.html",{"slist":info})
def software_delete(request):
    info = Software.objects.all()
    d = Software.objects.filter(id=request.GET['id']).delete()
    return render(request,"software.html",{"slist":info})

"""
str = 'SELECT * FROM Employee WHERE eid="' + request.POST["eid"] + '"'
        p = (Employee.objects.raw(str))
        found = False
        for x in p:
            found = True
        if (found):
            k = {"eid": request.POST['eid'], "ename": request.POST['ename'], "econtact": request.POST['econtact']}
            return render(request, "index.html",
                          {"form": k, "errormessage": 'This eid exist already' + request.POST['eid'],
                           "depts": fetchAllDepartments()})

        form = Employee(eid=request.POST['eid'], ename=request.POST['ename'], econtact=request.POST['econtact'],
                        depid=request.POST['depid'])
        form.save()
    if request.method == 'GET':
        # form = Employee.objects.all()
        # p = (Employee.objects.raw('update * FROM Employee WHERE dname'))
        return render(request, "dataView.html", {"form_list": info})
    return render(request, "dataView.html", {"form_list": info})"""