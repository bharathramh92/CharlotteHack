import csv
from search.models import Hospital


def dump():
    with open("search/ProcessedData.csv", "r") as a_file:
        reader = csv.reader(a_file)
        keys = "ProviderID,MORT_30_AMI,MORT_30_HF,MORT_30_PN,PSI_90_SAFETY,IMM_2,PN_6,SCIP_CARD_2,SCIP_INF_2,SCIP_INF_3,SCIP_INF_9,SCIP_VTE_2,AMI_7A,HAI1,HAI2,HAI3,HAI4,H_CLEAN_HSP_A_P,H_COMP_1_A_P,H_COMP_2_A_P,H_COMP_3_A_P,H_COMP_4_A_P,H_COMP_5_A_P,H_COMP_7_A,H_COMP_7_SA,H_QUIET_HSP_A_P,H_CLEAN_QUIET,H_COMP_7,MSPB_1,HospitalName,Address,City,State,ZIPCode,CountyName,PhoneNumber,HospitalType,HospitalOwnership,EmergencyServices"
        keys_list = keys.split(",")
        i = 0
        for row in reader:
            if i<700:
                i += 1
                continue
            data_dict = {}
            for i in range(len(keys_list)):
                data_dict[keys_list[i]] = row[i]
            print(data_dict["ProviderID"])
            try:
                Hospital.objects.get_or_create(**data_dict)
            except Exception:
                pass
