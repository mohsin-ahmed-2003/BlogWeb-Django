from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    blog_image = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=55, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
            # on_deletemodels.CASECADE = if deleting the author it will delete author's blog
            # on_deletemodels.POTECT = IT WILL NOT ALLOW the author TO BE DELETED
            # on_deletemodels.SET_NULL = IF author is deleted then it will set the column blank
    created_at = models.DateTimeField(default=timezone.now)
    content = RichTextField()

    def __str__(self):
        return self.title


    