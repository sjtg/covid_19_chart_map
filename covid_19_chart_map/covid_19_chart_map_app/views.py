# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def covid(request):
    

    countries_name = {}


    # Country 
    if 'countryname' in request.GET:
        countryname = request.GET['countryname']
        countryname = countryname.title()
        url = 'https://covid19.mathdro.id/api/countries/%s' % countryname
        response = requests.get(url)
        countries_name = response.json()


   
    
  
    return render(request, 'core/index.html', {'countries_name': countries_name, })


def pie_chart(request):
    labels = []
    data = []

    queryset = {}
    for countrys in queryset:
        countrys = request.GET['countrys']
        url = 'https://covid19.mathdro.id/api/countries/%s' % countrys
        response = requests.get(url)
        queryset = response.json()
        labels.append(country.confirmed)
        data.append(country.recovered)

    return render(request, 'core/index.html', {
        'labels': labels,
        'data': data,
        'queryset': queryset
    })
