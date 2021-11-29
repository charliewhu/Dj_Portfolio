from django.contrib import admin
from django.apps import apps
from portfolio.models import CVRole, CVRoleItem, Intro, Project_Tag, Project, RoleDescription, Tag, TagCategory


app = apps.get_app_config('portfolio')



class Project_TagInline(admin.TabularInline):
    model = Project_Tag

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        Project_TagInline,
    ]


class CVRoleItemInline(admin.TabularInline):
    model = CVRoleItem

class CVRoleAdmin(admin.ModelAdmin):
    inlines = [
        CVRoleItemInline,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Project_Tag)
admin.site.register(TagCategory) 
admin.site.register(Intro) 
admin.site.register(RoleDescription) 
admin.site.register(CVRole, CVRoleAdmin) 
admin.site.register(CVRoleItem) 

# for model_name, model in app.models.items():
#     admin.site.register(model)

