from django import forms

class FiltersForm(forms.Form):
    node_id = forms.IntegerField(required=False, label="Entity ID:")
    entity_type = forms.ChoiceField(required=False, label="Entity Type:", 
        choices={"PE":"Person", "ORG":"Organisation", "LO":"Location", "TEL":"Telecom", "VE":"Vehicle"})
    entity_name = forms.CharField(required=False, label="Entity Name Includes:")
    report_id = forms.IntegerField(required=False, label="Report ID:")
    creation_date_start = forms.DateTimeField(required=False, label="Created After:")
    creation_date_end = forms.DateTimeField(required=False, label="Created Before:")