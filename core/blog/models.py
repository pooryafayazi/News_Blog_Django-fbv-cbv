from django.db import models
from django.urls import reverse
# from taggit.managers import TaggableManager

# Create your models here.



class Post(models.Model):
    image = models.ImageField(upload_to='blog/%Y/%m/%d/',null=True, blank=True)
    author = models.ForeignKey('accounts.Profile', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    # topic = models.ForeignKey('homepage.Topic', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    # tags = TaggableManager()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    counted_views = models.IntegerField(default=0) # default=0
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)
        # verbose_name = "پست"
        # verbose_name_plural = "پست ها"
    def __str__(self):
        return f'{self.title} - {self.id}'
    
    def get_snippet(self):
        return self.content[:10]
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

