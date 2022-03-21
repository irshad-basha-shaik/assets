from django.urls import path,include
from . import views
urlpatterns = [
    path('assetapp', views.index, name='home'),
    path('', views.home, name='home1'),
    path('checkSerialNumber', views.checkSerialNumber, name='checkSerialNumber'),

    path('assets', views.index, name='assets'),
    path('assets_entry', views.new, name='entry'),
    path('assets_edit/<int:id>',views.edit,name='edit'),
    path('assets_delete/<int:id>',views.delete,name='delete'),
    path('it_assets', views.it_assets, name='it_assets'),
    path('connection', views.connection, name='pingmodel-list'),
    path('pingmodelbase', views.PingModelBase.as_view(), name='pingmodel_base'),
    path('create', views.connection_new, name='connection_new'),
    path('update/<int:pk>', views.PingModelUpdate.as_view(), name='pingmodel-detail'),
    path('delete/<int:pk>', views.PingModelDelete.as_view(), name='pingmodel-list'),

]

'''
    path('wifi',views.wifi_index,name='wifi'),
    path('wifi_entry',views.wifi,name='wifi_entry'),
    path('wifi_edit/<int:id>',views.wifi_edit,name='wifi_edit'),
    path('wifi_delete/<int:id>',views.wifi_delete,name='wifi_delete'),

    path('firewall',views.firewall_index,name='firewall'),
    path('firewall_entry',views.firewall,name='firewall_entry'),
    path('firewall_edit/<int:id>',views.firewall_edit,name='firewall_edit'),
    path('firewall_delete/<int:id>',views.firewall_delete,name='firewall_delete'),

    path('vcc', views.vcc_index, name='vcc'),
    path('vcc_entry', views.vcc, name='vcc_entry'),
    path('vcc_edit/<int:id>', views.vcc_edit, name='vcc_edit'),
    path('vcc_delete/<int:id>', views.vcc_delete, name='vcc_delete'),

    path('printer', views.printer_index, name='printer'),
    path('printer_entry', views.printer, name='printer_entry'),
    path('printer_edit/<int:id>', views.printer_edit, name='printer_edit'),
    path('printer_delete/<int:id>', views.printer_delete, name='printer_delete'),
'''
