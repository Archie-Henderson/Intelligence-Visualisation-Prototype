from django import forms
from data_processing.models import Entity

class FiltersForm(forms.Form):
    form_behaviour = forms.BooleanField(required=False)
    node_id = forms.IntegerField(required=False, label="Entity ID:")
    entity_type = forms.ChoiceField(required=False, label="Entity Type:", 
        choices=[("", "---------")] + Entity.ENTITY_TYPES)
    entity_name = forms.CharField(required=False, label="Entity Name Includes:")
    report_id = forms.IntegerField(required=False, label="Report ID:")
    creation_date_start = forms.DateTimeField(required=False, label="Created After:")
    creation_date_end = forms.DateTimeField(required=False, label="Created Before:")