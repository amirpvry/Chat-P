# Generated by Django 5.0 on 2024-02-28 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
