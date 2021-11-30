from django.db import models
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO

class TagCategory(models.Model):
    name        = models.CharField(max_length=100)
    hierarchy   = models.IntegerField(null=True, unique=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name        = models.CharField(max_length=100)
    tagcategory = models.ForeignKey(TagCategory, related_name='tag', 
        on_delete=models.DO_NOTHING, null=True, blank=True)
    icon_class  = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    name            = models.CharField(max_length=100)
    content         = models.TextField()
    date_created    = models.DateField()
    url             = models.URLField(max_length=200, null=True, blank=True)
    github_url      = models.URLField(max_length=200, null=True, blank=True)
    hierarchy       = models.IntegerField(null=True, unique=True)
    slug            = models.SlugField(max_length=20, null=True)
    image           = models.ImageField(upload_to='images', null=True, blank=True)
    tags            = models.ManyToManyField(Tag, related_name='tag',
        through='Project_Tag', 
        )

    def save(self, *args, **kwargs):
        """resize image on upload"""
        super().save(*args, **kwargs)
        memfile = BytesIO()
        img = Image.open(self.image)
        if img.height > 800 or img.width > 800:
            output_size = (400, 400)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, 'JPEG', quality=95)
            default_storage.save(self.image.name, memfile)
            memfile.close()
            img.close()

    def __str__(self):
        return self.name


class Project_Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag     = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.name} ' - ' {self.tag.name}"


class Intro(models.Model):
    #the welcome text onsite
    content   = models.TextField()
    hierarchy = models.IntegerField(null=True, unique=True)


class RoleDescription(models.Model):
    #brief strapline under my name
    content = models.CharField(max_length=100)


class CVRole(models.Model):
    title      = models.CharField(max_length=100)
    company    = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date   = models.DateField(null=True, blank=True)
    overview   = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class CVRoleItem(models.Model):
    cv_role = models.ForeignKey(CVRole, on_delete=models.CASCADE, related_name='roleitems')
    content = models.TextField()