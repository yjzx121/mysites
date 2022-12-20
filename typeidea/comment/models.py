from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'Normal'),
        (STATUS_DELETE, 'Delete'),
    )
    target = models.ForeignKey(Post, verbose_name="Comment Target")
    content = models.CharField(max_length=2000, verbose_name="Content")
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    website = models.URLField(verbose_name="Website")
    email = models.EmailField(verbose_name="Email")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="Status")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    class Meta:
        verbose_name = verbose_name_plural = "Comment"
