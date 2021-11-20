from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('assets', views.index, name='home'),
    path('assets_entry', views.new, name='home'),
    path('assets_edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]
'''
urlpatterns = [
    
    path('assets',views.assets,name='assets'),
    path('assets_entry',views.assets_entry,name='assets_entry'),
    path('asaveform',views.asaveform,name='asaveform'),
    path('editform',views.editform,name='editform'),
    path('a_edit',views.a_edit,name='a_edit'),
    path('adelete',views.adelete,name='adelete'),

    path('assets_types', views.assets_types, name='assets_types'),
    path('atype_entry', views.atype_entry, name='atype_entry'),
    path('asset_type_saveform', views.asset_type_saveform, name='asset_type_saveform'),
    path('atype_edit', views.atype_edit, name='atype_edit'),
    path('atype_editform', views.atype_editform, name='atype_editform'),
    path('atype_delete', views.atype_delete, name='atype_delete'),

    path('ops',views.ops,name='ops'),
    path('ops_entry',views.ops_entry,name='ops_entry'),
    path('ops_saveform',views.ops_saveform,name='ops_saveform'),
    path('ops_edit',views.ops_edit,name='ops_edit'),
    path('ops_editform',views.ops_editform,name='ops_editform'),
    path('ops_delete',views.ops_delete,name='ops_delete'),

    path('acategory',views.acategory,name='acategory'),
    path('acategory_entry',views.acategory_entry,name='acategory_entry'),
    path('acategory_saveform',views.acategory_saveform,name='acategory_saveform'),
    path('acategory_edit',views.acategory_edit,name='acategory_edit'),
    path('acategory_editform',views.acategory_editform,name='acategory_editform'),
    path('acategory_delete',views.acategory_delete,name='acategory_delete'),

    path('astatus',views.astatus,name='astatus'),
    path('astatus_entry',views.astatus_entry,name='astatus_entry'),
    path('astatus_saveform',views.astatus_saveform,name='astatus_saveform'),
    path('astatus_edit',views.astatus_edit,name='astatus_edit'),
    path('astatus_editform',views.astatus_editform,name='astatus_editform'),
    path('astatus_delete',views.astatus_delete,name='astatus_delete'),

    path('location',views.location,name='location'),
    path('location_entry',views.location_entry,name='location_entry'),
    path('location_saveform',views.location_saveform,name='location_saveform'),
    path('location_edit',views.location_edit,name='location_edit'),
    path('location_editform',views.location_editform,name='location_editform'),
    path('location_delete',views.location_delete,name='location_delete'),

    path('software', views.software, name='software'),
    path('software_entry', views.software_entry, name='software_entry'),
    path('software_saveform', views.software_saveform, name='software_saveform'),
    path('software_edit', views.software_edit, name='software_edit'),
    path('software_editform', views.software_editform, name='software_editform'),
    path('software_delete', views.software_delete, name='software_delete'),

]
'''