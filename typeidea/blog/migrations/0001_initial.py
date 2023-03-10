# Generated by Django 4.1.3 on 2022-12-20 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Normal'), (0, 'Delete')], default=1, verbose_name='Status')),
                ('is_nav', models.BooleanField(default=False, verbose_name='If is it navigate')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Categroy',
                'verbose_name_plural': 'Categroy',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Normal'), (0, 'Delete')], default=1, verbose_name='Status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Label',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='Summary')),
                ('content', models.TextField(help_text='Text must be MarkDown', verbose_name='Text')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Normal'), (0, 'Delete'), (2, 'Draft')], default=1, verbose_name='Status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('tag', models.ManyToManyField(to='blog.tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Article',
                'ordering': ['-id'],
            },
        ),
    ]
