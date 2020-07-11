from django.shortcuts import render, redirect
from .forms import reportForm
from .models import myForm
from django.contrib.auth.decorators import login_required

# from django.

# Create your views here.


@login_required
def displayForm(request):
    if request.method == 'POST':
        print('in POst')
        form = reportForm(request.POST)
        print('before is valid')
        if form.is_valid():
            print('afer is valid')
            formData = myForm(
                Location=form.cleaned_data.get('Location'),
                Incident_desc=form.cleaned_data.get('Incident_desc'),
                DateOfAcci=form.cleaned_data.get('DateOfAcci'),
                TimeOfAcci=form.cleaned_data.get('TimeOfAcci'),
                incident_loc=form.cleaned_data.get('incident_loc'),
                initial_seve=form.cleaned_data.get('initial_seve'),
                suspected_cause=form.cleaned_data.get('suspected_cause'),
                immediate_act=form.cleaned_data.get('immediate_act'),
                incident_type=form.cleaned_data.get('incident_type'),
                reporeted_by=request.user,
            )
            print('after form.reporeted_by ')
            formData.save()
            print('saved')
            return redirect('register')
    form = reportForm()
    return render(request, 'mainForms/form.html', {'form': form})
