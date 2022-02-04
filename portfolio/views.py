from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch
from portfolio.models import CVRole, Intro, Journey, TagCategory, Project, Project_Tag

# Create your views here.

def home(request):
    intro    = Intro.objects.all().order_by('hierarchy')

    context = {
        'intro':intro,
    }
    return render(request, 'portfolio/main/index.html', context)


def journey(request):
    journey    = Journey.objects.all()

    context = {
        'journey':journey,
    }
    return render(request, 'portfolio/main/journey.html', context)


def toolbox(request):
    tagcats  = TagCategory.objects.all().prefetch_related('tag').order_by('hierarchy')

    context = {
        'tagcats':tagcats,
    }
    return render(request, 'portfolio/main/toolbox.html', context)


def projects(request):
    projects = Project.objects.all().prefetch_related('tags').order_by('-date_created')

    context = {
        'projects':projects,
    }
    return render(request, 'portfolio/main/projects.html', context)


def experience(request):
    cvrole   = CVRole.objects.all().prefetch_related('roleitems').order_by('-start_date')

    context = {
        'cvrole':cvrole,
    }
    return render(request, 'portfolio/main/experience.html', context)


    