from distutils.command.upload import upload
import email
from enum import auto
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):

        return self.title
#New model
class News(models.Model):
    category_create = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

#Comment model

class Comment(models.Model):
    news =models.ForeignKey(News, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment