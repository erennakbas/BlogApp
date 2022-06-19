from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
class Blog(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
