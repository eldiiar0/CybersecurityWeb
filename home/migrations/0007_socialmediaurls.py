# Generated by Django 5.0.6 on 2024-06-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(max_length=255)),
                ('facebook', models.URLField(max_length=255)),
                ('twitter', models.URLField(max_length=255)),
            ],
        ),
    ]
