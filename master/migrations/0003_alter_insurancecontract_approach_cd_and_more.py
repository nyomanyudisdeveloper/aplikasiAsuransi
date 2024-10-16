# Generated by Django 5.1.1 on 2024-10-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master", "0002_insurancecontract_pattern"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insurancecontract",
            name="approach_cd",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="begin_cov_dt",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="branch_cd",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="cedeg_flg",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="channel_cd",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="cohort_id",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="commision_amt",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="currency_cd",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="end_cov_dt",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="endorsement_dt",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="endorsement_type_cd",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="entity_id",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="insurance_contract_id",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="insurance_type",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="interco_cd",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="interco_flg",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="issue_dt",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="lgd",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="pd",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="periode_pembayaran",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="prem_amt",
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="product_id",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="product_line_id",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="profitability",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="reins_prop_cover_flg",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="reins_treaty_flg",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="reporting_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="insurancecontract",
            name="transition_reporting_approach_cd",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
