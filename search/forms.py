from django import forms

HOSP_CHOICES_Dict = {'a': "All", 'gf':'Government - Federal', "gda":"Government - Hospital District or Authority",
                "gl": "Government - Local", "gs": "Government - State", "ph": "Physician",
                "pr": "Proprietary", "tr": "Tribal", "vnc": "Voluntary non-profit - Church",
                "vnpo": "Voluntary non-profit - Other", "vnpp": "Voluntary non-profit - Private"}
EMERGENCY_CHOICE = {"yes": "Yes", "no": "No"}
CRITERIA_CHOICE = {"all":"All", "co":"Clinical Outcomes", "cp": "Clinical Process",
                   "cm": "Complications", "pe":"Patient Experience", "sr":"Expense"}


class SearchForm(forms.Form):
    zipcode = forms.CharField(label='Zipcode',
                              max_length=10,
                              required=True)

    hosp_type = forms.ChoiceField(label="Hospital Type",
                                  choices=sorted(tuple(HOSP_CHOICES_Dict.items()), key=lambda x: x[0]),
                                  required=True)

    emergency = forms.ChoiceField(label="Emergency?",
                                  choices=tuple(EMERGENCY_CHOICE.items()),
                                  required=True)
    criteria = forms.ChoiceField(label="Criteria",
                                 choices=sorted(tuple(CRITERIA_CHOICE.items()), key=lambda x: x[0]),
                                 required=True)