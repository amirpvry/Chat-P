# Generated by Django 5.0 on 2024-02-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/blog/aaaaa.jpg', upload_to='blog/'),
        ),
    ]
