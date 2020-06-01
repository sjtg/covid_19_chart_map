# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def covid(request):
    # labels = []
    # data = []

    countries_name = {}
    if 'countryname' in request.GET:
        countryname = request.GET['countryname']
        url = 'https://covid19.mathdro.id/api/countries/%s' % countryname
        response = requests.get(url)
        countries_name = response.json()
    return render(request, 'core/index.html', {'countries_name': countries_name})




    # queryset = City.objects.order_by('-population')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })