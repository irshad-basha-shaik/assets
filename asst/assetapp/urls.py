from django.urls import path
from . import views

urlpatterns = [
    path('assets_types',views.assets_types,name='assets_types'),
    path('atype_entry',views.atype_entry,name='atype_entry'),
    path('asset_type_saveform',views.asset_type_saveform,name='asset_type_saveform'),
    path('atype_edit',views.atype_edit,name='atype_edit'),
    path('atype_editform',views.atype_editform,name='atype_editform'),
    path('atype_delete',views.atype_delete,name='atype_delete'),

    path('assets',views.assets,name='assets'),
    path('new_assets',views.new_assets,name='new_assets'),
    path('asaveform',views.asaveform,name='asaveform'),
    path('aeditform',views.aeditform,name='aeditform'),
    path('aedit',views.aedit,name='aedit'),
    path('adelete',views.adelete,name='adelete'),


]
