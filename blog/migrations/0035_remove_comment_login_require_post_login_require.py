# Generated by Django 5.0.4 on 2024-05-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_alter_comment_options_comment_login_require'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='login_require',
        ),
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
