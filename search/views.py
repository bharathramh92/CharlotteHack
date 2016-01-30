from django.shortcuts import render
from search.forms import SearchForm
from search.models import Hospital
from django.db.models import Q
from search.forms import CRITERIA_CHOICE, HOSP_CHOICES_Dict, EMERGENCY_CHOICE
# Create your views here.


def rank(zipcode, hosp_type, emergency, criteria):
    hosp_types_dist = [x['HospitalOwnership'] for x in Hospital.objects.values('HospitalOwnership').distinct()]
    print("hosp_type ", hosp_type)
    if hosp_type == "a":
        hosp_ownership_types = hosp_types_dist
    else:
        hosp_ownership_types = [HOSP_CHOICES_Dict[hosp_type]]
    print(hosp_ownership_types)
    # data = Hospital.objects.all()
    criteria_map = {"co":["MORT_30_AMI","MORT_30_HF","MORT_30_PN","PSI_90_SAFETY"],
                    "cp": ["IMM_2","PN_6","SCIP_CARD_2","SCIP_INF_2","SCIP_INF_3","SCIP_INF_9","SCIP_VTE_2","AMI_7A"],
                       "cm": ["HAI1","HAI2","HAI3","HAI4"],
                    "pe":["H_CLEAN_HSP_A_P","H_COMP_1_A_P","H_COMP_2_A_P","H_COMP_3_A_P",
                          "H_COMP_4_A_P","H_COMP_5_A_P","H_COMP_7_A","H_COMP_7_SA","H_QUIET_HSP_A_P"],
                    "sr":["MSPB_1"]}



    data = Hospital.objects.filter(EmergencyServices__iexact = emergency, HospitalOwnership__in=hosp_ownership_types)
    keys = "MORT_30_AMI,MORT_30_HF,MORT_30_PN,PSI_90_SAFETY,IMM_2,PN_6,SCIP_CARD_2,SCIP_INF_2,SCIP_INF_3,SCIP_INF_9,SCIP_VTE_2,AMI_7A,HAI1,HAI2,HAI3,HAI4,H_CLEAN_HSP_A_P,H_COMP_1_A_P,H_COMP_2_A_P,H_COMP_3_A_P,H_COMP_4_A_P,H_COMP_5_A_P,H_COMP_7_A,H_COMP_7_SA,H_QUIET_HSP_A_P,H_CLEAN_QUIET,H_COMP_7,MSPB_1"
    keys_list = keys.split(",")
    criteria = [criteria]

    def weight(dt):
        nonlocal criteria
        x = 0
        dt = dt.__dict__
        # for key in keys_list:

        if "all" in criteria:
            criteria = list(CRITERIA_CHOICE.keys())


        # s = 0
        print(criteria)
        for c in criteria:
            if c == "all":
                continue
            print(c)
            for value in criteria_map[c]:
                x += int(dt[value])

            # print(key)
            # x += int(dt[key])
        return x

        # def weight(dt):
        #     x = 0
        #     dt = dt.__dict__
        #     for key in keys_list:
        #
        #         print(key)
        #         x+=int(dt[key])
        #     return x




    data = sorted(data, key=weight)
    return data[:10]


def index(request):
    # if this is a POST request we need to process the form data
    # dump()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("here")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            zipcode = form.cleaned_data["zipcode"]
            hosp_type = form.cleaned_data["hosp_type"]
            emergency = form.cleaned_data["emergency"]
            criteria = form.cleaned_data["criteria"]
            print(form.errors)
            data = rank(zipcode, hosp_type, emergency, criteria)

            return render(request, "search/result.html", {'form': form, 'data': data})
        # else:
        #     print("invalid form")
        #     print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "search/index_.html", {'form': form})