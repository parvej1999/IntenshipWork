from django import forms
from .models import myForm
from django.forms.widgets import DateInput, TimeInput, Textarea
from crispy_forms.helper import FormHelper
from django.utils import timezone


class MyTextarea(Textarea):
    def __init__(self, attrs={}):
        attrs.update({'cols': '70', 'rows': '20'})
        super(MyTextarea, self).__init__(attrs)


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
            'Incident_desc': forms.Textarea(attrs={'rows': 2, 'cols': 15, 'placeholder': 'Description About Incident!...'}),
            'incident_loc': forms.Textarea(attrs={'rows': 2, 'cols': 15, 'placeholder': 'Incident Location!...'}),
            'suspected_cause': forms.Textarea(attrs={'rows': 2, 'cols': 15, 'placeholder': 'Supected Cause Of Accident!...'}),
            'immediate_act': forms.Textarea(attrs={'rows': 2, 'cols': 15, 'placeholder': 'Immediate Actions Taken By You!...'}),
        }
