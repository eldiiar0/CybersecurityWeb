# Generated by Django 5.0.6 on 2024-05-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0002_membersresources_membersevents_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembersMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
