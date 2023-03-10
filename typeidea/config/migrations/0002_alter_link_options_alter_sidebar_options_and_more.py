# Generated by Django 4.1.3 on 2022-12-28 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
        migrations.AlterModelOptions(
            name='sidebar',
            options={'verbose_name': '侧边栏', 'verbose_name_plural': '侧边栏'},
        ),
        migrations.RemoveField(
            model_name='link',
            name='herf',
        ),
        migrations.AddField(
            model_name='link',
            name='href',
            field=models.URLField(default='', verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='link',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='link',
            name='weight',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重高展示顺序靠前', verbose_name='权重'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.CharField(blank=True, help_text='如果设置的不是HTML类型， 可为空', max_length=500, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论')], default=1, verbose_name='展示类型'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]
