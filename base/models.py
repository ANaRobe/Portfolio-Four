"""Database Tables"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


class Cocktail(models.Model):
    """Cocktail recipe blueprint"""
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = CloudinaryField('image', default='placeholder')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remarks', null=False, blank=False,)
    alcoholic = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='cocktail_hearts', blank=True)
    ingredients = models.TextField(null=False, blank=False)
    steps = models.TextField(null=False, blank=False)
    mixing_time = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(60)])
    status = models.IntegerField(choices=STATUS, default=1)
    publish_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)

    SWEET = 'sweet'
    BITTER = 'bitter'
    SOUR = 'sour'
    SALTY = 'salty'
    UMAMI = 'umami'
    COOL = 'cool'
    HOT = 'hot'

    COCKTAIL_TASTE = [
        (SWEET, 'sweet'),
        (BITTER, 'bitter'),
        (SOUR, 'sour'),
        (SALTY, 'salty'),
        (UMAMI, 'umami'),
        (COOL, 'cool'),
        (HOT, 'hot')
    ]

    taste = models.CharField(max_length=50, choices=COCKTAIL_TASTE, default=COOL, blank=False)

    class Meta:
        """Orders articles by title """
        ordering = ['title']

    def __str__(self):
        return f"{self.title} | {self.user}"

    def number_of_likes(self):
        """Returns the total number of likes for each published cocktail"""
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('cocktail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Remark(models.Model):
    """Layout for comments"""
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='remarks', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remarks_user')
    text = models.TextField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Orders articles by published date descendant """
        ordering = ['-publish_date']

    def __str__(self):
        return f"Comment{self.text} by {self.user}"

