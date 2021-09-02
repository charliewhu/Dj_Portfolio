from django.contrib import admin
from django.apps import apps
from portfolio.models import Project_Tag, Project, Tag, TagCategory


app = apps.get_app_config('portfolio')


class Project_TagInline(admin.TabularInline):
    model = Project_Tag


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        Project_TagInline,
    ]



admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Project_Tag)
admin.site.register(TagCategory)

# for model_name, model in app.models.items():
#     admin.site.register(model)

