# Generated by Django 5.0 on 2024-02-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/blog/images.jpg', upload_to='blog/'),
        ),
    ]
