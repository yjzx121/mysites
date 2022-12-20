from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'Normal'),
        (STATUS_DELETE, 'Delete'),
    )

    name = models.CharField(max_length=50, verbose_name="Name")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="Status")
    is_nav = models.BooleanField(default=False, verbose_name="If is it navigate")
    owner = models.ForeignKey(User, verbose_name="Owner")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Categroy"


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'Normal'),
        (STATUS_DELETE, 'Delete'),
    )

    name = models.CharField(max_length=10, verbose_name="Name")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="Status")
    owner = models.ForeignKey(User, verbose_name="Owner")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Label"


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'Normal'),
        (STATUS_DELETE, 'Delete'),
        (STATUS_DRAFT, 'Draft'),
    )

    title = models.CharField(max_length=255, verbose_name="Title")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="Summary")
    content = models.TextField(verbose_name="Text", help_text="Text must be MarkDown")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="Status")
    category = models.ForeignKey(Category, verbose_name="Category")
    tag = models.ManyToManyField(Tag, verbose_name="Tag")
    owner = models.ForeignKey(User, verbose_name="Owner")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Article"
        ordering = ['-id']

