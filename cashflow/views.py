from django.shortcuts import render, redirect
from django.http import HttpResponse
from master.models import InsuranceContract, Pattern

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        list_insurance_contracts = InsuranceContract.objects.values("id","insurance_contract_id","product_id","cohort_id","cedeg_flg","endorsement_type_cd","begin_cov_dt","end_cov_dt","endorsement_dt","prem_amt","reporting_date","periode_pembayaran")
        temp_list = []
        for insurance_contract in list_insurance_contracts:
            temp_list.append({
                "id": insurance_contract['id'] if insurance_contract['id'] is not  None else -1  ,
                "insurance_contract_id":insurance_contract['insurance_contract_id'] if insurance_contract['insurance_contract_id'] is not None else "None",
                "product_id" : insurance_contract['product_id'] if insurance_contract['product_id'] is not None else "None", 
                "cohort_id": insurance_contract["cohort_id"],
                "cedeg_flg": insurance_contract["cedeg_flg"],
                "endorsement_type_cd": insurance_contract["endorsement_type_cd"],
                "begin_cov_dt": insurance_contract["begin_cov_dt"].strftime('%m/%d/%Y') if insurance_contract["begin_cov_dt"] is not None else "",
                "end_cov_dt": insurance_contract["end_cov_dt"].strftime('%m/%d/%Y') if insurance_contract["end_cov_dt"] is not None else "",
                "endorsement_dt": insurance_contract["endorsement_dt"].strftime('%m/%d/%Y') if insurance_contract["endorsement_dt"] is not None else "",
                "prem_amt": insurance_contract["prem_amt"],
                "reporting_date": insurance_contract["reporting_date"].strftime('%m/%d/%Y') if insurance_contract["reporting_date"] is not None else "",
                "periode_pembayaran": insurance_contract["periode_pembayaran"]
            })
        context ={
            "list_insurance_contracts":temp_list
        }
        
        return render(request,"cashflow/premi.html",context)
    else:
        return redirect("/accounts/login")
