from django.shortcuts import render

from mainapp.models import News


def index(request):
	return render(request, 'base.html', {'news': News.objects.all()})
