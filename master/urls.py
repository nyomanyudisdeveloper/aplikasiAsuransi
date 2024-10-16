from django.urls import path

from . import  views

app_name = 'master'

urlpatterns = [
    path("pattern",views.pattern, name="pattern"),
    path("pattern/import_template", views.pattern_import_data_from_template, name="pattern_import_template"),
    path("pattern/export_template", views.pattern_export_template, name="pattern_export_template"),
    path("insurance_contract/", views.insurance_contract, name="insurance_contract"),
    path("insurance_contract/export_template", views.insurance_contract_export_template, name="insurance_contract_export_template"),
    path("insurance_contract/import_template", views.insurance_contract_import_template, name="insurance_contract_import_template"),
    path("assumption/", views.assumption, name="assumption"),
    path("assumption/export_template", views.assumption_export_template, name="assumption_export_template"),
    path("assumption/import_template", views.assumption_import_data_from_template, name="assumption_import_template"),
]

