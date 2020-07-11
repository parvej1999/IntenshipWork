from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
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


class myForm(models.Model):
    Location = models.CharField(
        verbose_name='Location', max_length=3, choices=Location)
    Incident_desc = models.TextField(verbose_name='Incident Description')
    DateOfAcci = models.DateField(verbose_name='Date Of Incident')
    TimeOfAcci = models.TimeField(verbose_name='Time Of Incident')
    incident_loc = models.TextField(verbose_name='Incident Location')
    initial_seve = models.CharField(
        verbose_name='Initial Severity', max_length=1, choices=Severity)
    suspected_cause = models.TextField(verbose_name='Suspected Cause')
    immediate_act = models.TextField(verbose_name='Immediate Actions Taken')
    incident_type = MultiSelectField(
        verbose_name='Sub Incident Types', choices=incident_type)
    reporeted_by = models.ForeignKey(
        User, verbose_name='Reported By', on_delete=models.CASCADE)

    def __str__(self):
        return self.reporeted_by.username
