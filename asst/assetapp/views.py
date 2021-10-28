from django.shortcuts import render
from .models import Assets_types,Assets

# Create your views here.
def assets_types(request):
    d=Assets_types.objects.all()
    return render(request,"asset_types.html",{"depts":d})
def atype_entry(request):
    return render(request,"atype_entry.html",{})
def asset_type_saveform(request):
    d=Assets_types.objects.all()
    form=Assets_types(dname=request.POST['dname'],code=request.POST['code'])
    form.save()
    return render(request,"asset_types.html",{"depts":d})
def atype_edit(request):
    id=request.GET['id']
    form=Assets_types.objects.get(id=id)
    return render(request,"atype_edit.html",{"form":form})
def atype_editform(request):
    info = Assets_types.objects.all()
    d = Assets_types.objects.filter(id=request.POST['id']).update(dname=request.POST['dname'], email=request.POST['email'],
                                                               code=request.POST['code'])
    return render(request,"asset_types.html",{"form_list":info})
def atype_delete(request):
    info = Assets_types.objects.all()
    d = Assets_types.objects.filter(id=request.GET['id']).delete()
    return render(request,"asset_types.html",{"depts":d})

def assets(request):
    info = Assets.objects.all()

    return render(request, "assets.html", {"form_list": info})




def new_assets(request):

    return render(request,"new_assets.html",{})

def asaveform(request):
    info = Employees.objects.all()
    depts = Department.objects.all()
    if request.method == 'POST':
        form = Employees(name=request.POST['name'], email=request.POST['email'], mobile=request.POST['mobile'],
                         place=request.POST['place'], depid=request.POST['depid'])
        form.save()
        return render(request, "employees.html", {"form_list": info})


def aeditform(request):
    return render(request,"aeditform.html",{})

def aedit(request):
    return render(request,"aedit.html",{})

def adelete(request):
    return render(request,"adelete.html",{})
