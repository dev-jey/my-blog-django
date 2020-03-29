import os
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image')
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def cloudinary_image(self):
        return f"https://res.cloudinary.com/{os.environ.get('CLOUD_NAME', '')}/{self.image}"


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def cloudinary_image(self):
        return f"https://res.cloudinary.com/{os.environ.get('CLOUD_NAME', '')}/{self.image}"
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = HTMLField()
    category = models.ForeignKey(Category, related_name='articles',
                                 on_delete=models.CASCADE,
                                 blank=True, null=True)
    image = CloudinaryField('image')
    slug = models.SlugField(db_index=True, max_length=1000, default='',
                            editable=False,
                            unique=True, blank=True, primary_key=True)
    author = models.ForeignKey(User, related_name='articles',
                               on_delete=models.CASCADE,
                               blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cloudinary_image(self):
        return f"https://res.cloudinary.com/{os.environ.get('CLOUD_NAME', '')}/{self.image}"

    class Meta:
        '''Defines the ordering of the
         country if retrieved'''
        ordering = ('title',)

    def __str__(self):
        return self.title

    def generate_slug(self):
        """generating a slug for the title of the article
            eg: this-is-an-article"""
        slug = slugify(self.title)
        new_slug = slug
        s = 1
        while Article.objects.filter(slug=new_slug).exists():
            """increase value of slug by one"""
            new_slug = f'{slug}-{s}'
            s += 1
        return new_slug

    def save(self, *args, **kwargs):
        """create an article and save to the database"""
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)
