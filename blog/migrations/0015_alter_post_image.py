# Generated by Django 5.0 on 2024-02-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/hero-bg.jpg', upload_to='media/blog/'),
        ),
    ]
