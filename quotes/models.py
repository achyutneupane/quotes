from django.db import models
from django.shortcuts import render,reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
from django.contrib.auth.models import User


class MainMenu(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=60)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    slug = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    thumbup = models.ManyToManyField(User,related_name='likes', blank=True)
    thumbdown = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    @property
    def num_likes(self):
        return self.thumbup.all().count()



Like_Choices= (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(choices=Like_Choices, default='Like', max_length=10)
    thumbdown = models.IntegerField(default=0)

    def __str__(self):
        return self.post