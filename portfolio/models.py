from django.db import models
from PIL import Image


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
    image           = models.ImageField(null=True)
    tags            = models.ManyToManyField(Tag, related_name='tag',
        through='Project_Tag', 
        )

    def save(self):
        """resize image on upload"""
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name


class Project_Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag     = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.name} ' - ' {self.tag.name}"


