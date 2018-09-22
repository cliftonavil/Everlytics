
from django.db.models import Sum
from django.shortcuts import render, redirect
import json
from .models import Browsers
from .forms import CreateBrowsers
from .import forms


def home(request):
    #home page with form & Data retrival

    Browsers_final = []
    percentage_final = []

    tota_data = Browsers.objects.aggregate(Sum('Users'))
    group_by = Browsers.objects.values('Browsers').annotate(Sum('Users'))
    total = tota_data['Users__sum']

    for i in group_by:
        Browsers_final.append(i['Browsers'])
        percentage_calculated = (i['Users__sum'] / total) * 100
        percentage_final.append("%.3f" % percentage_calculated)

    data= Browsers.objects.values('Browsers').annotate(Sum('Users'))
    form = forms.CreateBrowsers(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = CreateBrowsers()
        return redirect('Highcharts:home')
    else:
        path = 'home.html'
    return render(request, path, {
                                    'data':data,
                                    'form': form ,
                                    'Browsers_final': Browsers_final,
                                    'percentage_final': percentage_final
                                })
