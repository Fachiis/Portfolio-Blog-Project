from django.shortcuts import render

from .models import Job


def homepage(request):
    jobs = Job.objects.all
    return render(request, 'home.html', {'jobs' : jobs})


    

