from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch
from portfolio.models import TagCategory, Project, Project_Tag

# Create your views here.

def home(request):
    tagcats = TagCategory.objects.all().prefetch_related('tag').order_by('hierarchy')
    projects = Project.objects.all().prefetch_related('tags')

    context = {
        'tagcats':tagcats,
        'projects':projects,
    }
    return render(request, 'portfolio/main/index.html', context)


    