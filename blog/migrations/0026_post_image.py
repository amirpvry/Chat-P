# Generated by Django 5.0 on 2024-02-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog/'),
        ),
    ]
