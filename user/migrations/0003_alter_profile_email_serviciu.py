# Generated by Django 4.1 on 2022-09-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_url_github_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_serviciu',
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]
