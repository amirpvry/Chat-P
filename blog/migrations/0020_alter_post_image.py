# Generated by Django 5.0 on 2024-02-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images.jpg', upload_to='blog/'),
        ),
    ]
