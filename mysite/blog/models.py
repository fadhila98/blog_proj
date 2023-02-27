from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from django.db import models
# from froala_editor.fields import FroalaField

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length= 1000, unique= True)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE,related_name= 'blog_posts')
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to = 'img',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blogmodel-detail", kwargs={"id": self.id})

