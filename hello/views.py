from django.shortcuts import render
from django.http import HttpResponse

import datetime

from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def dashboard(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "dashboard.html")


def create_download(request):

	app_download = AppDownload()
	app_download.longitude = -0.127758
	app_download.latitude = 51.507351
	app_download.downloaded_at = datetime.datetime.now()
	app_download.app_id = 'IOS_ALERT'
	app_download.save()

	return render(request, "dashboard.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
