# Generated by Django 5.0 on 2024-02-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/images.jpg', upload_to='blog/'),
        ),
    ]
