from django.shortcuts import render
import datetime


def home(request):
    now = datetime.datetime.now()
    data = {
        'now': now
    }
    return render(request, 'base.html', context=data)
# Create your views here.
