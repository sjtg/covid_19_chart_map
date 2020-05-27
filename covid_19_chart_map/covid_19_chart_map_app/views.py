# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def covid(request):
    user = {}
    if 'countryname' in request.GET:
        countryname = request.GET['countryname']
        url = 'https://covid19.mathdro.id/api/countries/%s' % countryname
        response = requests.get(url)
        user = response.json()
    return render(request, 'core/index.html', {'user': user})