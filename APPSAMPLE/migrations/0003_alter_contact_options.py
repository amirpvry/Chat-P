# Generated by Django 5.0.1 on 2024-04-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APPSAMPLE', '0002_rename_content_contact_count_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-create_date']},
        ),
    ]
