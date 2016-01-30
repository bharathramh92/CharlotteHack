# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('ProviderID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('MORT_30_AMI', models.FloatField(blank=True, max_length=5, null=True)),
                ('MORT_30_HF', models.FloatField(blank=True, max_length=5, null=True)),
                ('MORT_30_PN', models.FloatField(blank=True, max_length=5, null=True)),
                ('PSI_90_SAFETY', models.FloatField(blank=True, max_length=5, null=True)),
                ('IMM_2', models.FloatField(blank=True, max_length=5, null=True)),
                ('PN_6', models.FloatField(blank=True, max_length=5, null=True)),
                ('SCIP_CARD_2', models.FloatField(blank=True, max_length=5, null=True)),
                ('SCIP_INF_2', models.FloatField(blank=True, max_length=5, null=True)),
                ('SCIP_INF_3', models.FloatField(blank=True, max_length=5, null=True)),
                ('SCIP_INF_9', models.FloatField(blank=True, max_length=5, null=True)),
                ('SCIP_VTE_2', models.FloatField(blank=True, max_length=5, null=True)),
                ('AMI_7A', models.FloatField(blank=True, max_length=5, null=True)),
                ('HAI1', models.FloatField(blank=True, max_length=5, null=True)),
                ('HAI2', models.FloatField(blank=True, max_length=5, null=True)),
                ('HAI3', models.FloatField(blank=True, max_length=5, null=True)),
                ('HAI4', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_CLEAN_HSP_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_1_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_2_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_3_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_4_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_5_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_7_A', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_7_SA', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_QUIET_HSP_A_P', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_CLEAN_QUIET', models.FloatField(blank=True, max_length=5, null=True)),
                ('H_COMP_7', models.FloatField(blank=True, max_length=5, null=True)),
                ('MSPB_1', models.FloatField(blank=True, max_length=5, null=True)),
                ('HospitalName', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('City', models.CharField(blank=True, max_length=20, null=True)),
                ('State', models.CharField(blank=True, max_length=20, null=True)),
                ('ZIPCode', models.CharField(blank=True, max_length=10, null=True)),
                ('CountyName', models.CharField(blank=True, max_length=50, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('HospitalType', models.CharField(blank=True, max_length=50, null=True)),
                ('HospitalOwnership', models.CharField(blank=True, max_length=50, null=True)),
                ('EmergencyServices', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
