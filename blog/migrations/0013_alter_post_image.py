# Generated by Django 5.0 on 2024-02-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/IMG_3865.jpg', upload_to='blog/'),
        ),
    ]
