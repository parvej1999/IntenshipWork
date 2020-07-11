from django import forms
from .models import myForm
from django.forms.widgets import DateInput, TimeInput

Location = (
    ('CHO', 'Corporate Head Office'),
    ('CBO', 'Corporate Branch Office'),
    ('HO', 'Home Office'),
    ('CS', 'Co-Working Space'),
    ('CVO', 'Corporate Virtual Office'),


)

Severity = (
    ('B', 'Bad'),
    ('S', 'serious'),
    ('U', 'unpleasant'),
    ('H', 'Harsh'),
    ('M', 'Mild'),
)

incident_type = (
    ('EI', 'Environmental Incident'),
    ('I', 'Injury/Illness'),
    ('PD', 'Property Damage'),
    ('V', 'Vehicle'),
    ('M', 'Mild'),
)


class reportForm(forms.ModelForm):

    class Meta:
        model = myForm
        fields = ['Location', 'Incident_desc', 'DateOfAcci', 'TimeOfAcci', 'incident_loc',
                  'initial_seve', 'suspected_cause', 'immediate_act', 'incident_type']
        widgets = {
            'DateOfAcci': DateInput(attrs={'type': 'date'}),
            'TimeOfAcci': TimeInput(attrs={'type': 'time'}),
        }
