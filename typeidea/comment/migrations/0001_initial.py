# Generated by Django 4.1.3 on 2022-12-20 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='Content')),
                ('nickname', models.CharField(max_length=50, verbose_name='Nickname')),
                ('website', models.URLField(verbose_name='Website')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Normal'), (0, 'Delete')], default=1, verbose_name='Status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Comment Target')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
            },
        ),
    ]
