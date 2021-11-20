
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AssetForm
from .models import AssetModel
# Create your views here.


def new(request):
    context = {}
    context['form'] = AssetForm()
    if request.method== 'POST':
       # form = SettingsForm(request.POST or None)
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
            #bj = form.save()
            #AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
            AssetModel.objects.filter(pk=id).update(processor_purchase_date=form.cleaned_data['processor_purchase_date'])

            return index(request)
    context['form'] = form
    return render(request,"assets_edit.html",context)
def delete(request,id):
    context = {}
    obj = get_object_or_404(AssetModel, id=id)
    obj.delete()
    return HttpResponseRedirect("/")


