from django.db import models

# Create your models here.
class Assumption(models.Model):
    name = models.CharField(max_length=200)
    ratio = models.FloatField(default=0.0)

class Pattern(models.Model):
    periode = models.IntegerField(default=0)
    claim_payment_pattern = models.FloatField(default=0.0)
    claim_incurred_pattern = models.FloatField(default=0.0)
    premium_payment_pattern = models.FloatField(default=0.0)
    month_1 = models.FloatField(default=0.0)
    month_2 = models.FloatField(default=0.0)
    month_3 = models.FloatField(default=0.0)
    month_4 = models.FloatField(default=0.0)
    month_5 = models.FloatField(default=0.0)
    month_6 = models.FloatField(default=0.0)
    month_7 = models.FloatField(default=0.0)
    month_8 = models.FloatField(default=0.0)
    month_9 = models.FloatField(default=0.0)
    month_10 = models.FloatField(default=0.0)
    month_11 = models.FloatField(default=0.0)
    month_12 = models.FloatField(default=0.0)

class InsuranceContract(models.Model):
    reporting_date = models.DateField(null=True)
    entity_id = models.IntegerField(default=0,null=True)
    insurance_contract_id = models.CharField(max_length=100,null=True)
    endorsement_type_cd = models.IntegerField(default=0,null=True)
    issue_dt = models.DateField(null=True)
    product_line_id = models.CharField(max_length=10,null=True)
    product_id = models.CharField(max_length=20,null=True)
    cohort_id = models.CharField(max_length=20,null=True)
    cedeg_flg = models.CharField(max_length=20,null=True)
    insurance_type = models.CharField(max_length=20,null=True)
    reins_prop_cover_flg = models.CharField(max_length=20,null=True)
    reins_treaty_flg = models.CharField(max_length=20,null=True)
    endorsement_dt = models.DateField(null=True)
    interco_cd = models.CharField(max_length=20,null=True)
    interco_flg = models.CharField(max_length=20,null=True)
    branch_cd = models.CharField(max_length=20,null=True)
    channel_cd = models.CharField(max_length=20,null=True)
    approach_cd = models.CharField(max_length=20,null=True)
    transition_reporting_approach_cd = models.CharField(max_length=20,null=True)
    begin_cov_dt = models.DateField(null=True)
    end_cov_dt = models.DateField(null=True)
    currency_cd =  models.CharField(max_length=20,null=True)
    prem_amt = models.BigIntegerField(default=0,null=True)
    commision_amt = models.IntegerField(default=0,null=True)
    pd = models.IntegerField(default=0,null=True)
    lgd = models.IntegerField(default=0,null=True)
    profitability = models.CharField(max_length=20,null=True)
    periode_pembayaran = models.IntegerField(default=0,null=True)
