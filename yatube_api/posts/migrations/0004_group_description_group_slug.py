# Generated by Django 5.1.7 on 2025-03-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=None, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
