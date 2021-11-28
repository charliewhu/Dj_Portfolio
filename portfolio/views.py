from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch
from portfolio.models import Intro, TagCategory, Project, Project_Tag

# Create your views here.

def home(request):
    intro    = Intro.objects.all().order_by('hierarchy')
    tagcats  = TagCategory.objects.all().prefetch_related('tag').order_by('hierarchy')
    projects = Project.objects.all().prefetch_related('tags').order_by('hierarchy')

    context = {
        'tagcats':tagcats,
        'projects':projects,
        'intro':intro,
    }
    return render(request, 'portfolio/main/index.html', context)


    