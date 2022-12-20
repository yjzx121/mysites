from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'Normal'),
        (STATUS_DELETE, 'Delete'),
    )

    title = models.CharField(max_length=50, verbose_name="Title")
    herf = models.URLField(verbose_name="Link")   # default longth is 200;
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="Status")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name="Weight",
                                         help_text="The ones with high weight are shown in the front")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Friendly Link"


class SideBar(models.Model):
    STATUS_SHOW= 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, 'Show'),
        (STATUS_HIDE, 'Hide'),
    )
    SIDE_TYPE = (
        (1, "HTML"),
        (2, "Newest article"),
        (3, 'Hottest article'),
        (4, 'Recent comments'),
    )

    title = models.CharField(max_length=50, verbose_name="Title")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name="Show Type")
    content = models.CharField(max_length=500, blank=True, verbose_name="Content",
                               help_text="If setting type is not HTML, can be blank")
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="Status")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Sidebar"






