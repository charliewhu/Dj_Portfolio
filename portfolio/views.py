from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch
from portfolio.models import CVRole, Intro, TagCategory, Project, Project_Tag

# Create your views here.

def home(request):
    intro    = Intro.objects.all().order_by('hierarchy')
    tagcats  = TagCategory.objects.all().prefetch_related('tag').order_by('hierarchy')
    projects = Project.objects.all().prefetch_related('tags').order_by('-date_created')
    cvrole   = CVRole.objects.all().prefetch_related('roleitems').order_by('-start_date')

    context = {
        'tagcats':tagcats,
        'projects':projects,
        'intro':intro,
        'cvrole':cvrole,
    }
    return render(request, 'portfolio/main/index.html', context)


    