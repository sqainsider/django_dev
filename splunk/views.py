
# splunk_dataValidation/views.py

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):

    # testcases = testcase.objects.all()
    # output = ', ' .join([m.title for m in movies])
    return render(request, 'splunk/index.html')
