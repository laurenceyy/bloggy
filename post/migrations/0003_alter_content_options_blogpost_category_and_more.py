# Generated by Django 5.0.7 on 2024-08-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_blogpost_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['content_type', 'blog_post']},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.CharField(default='not provided', max_length=500),
            preserve_default=False,
        ),
    ]
