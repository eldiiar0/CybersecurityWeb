# Generated by Django 5.0.6 on 2024-05-30 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0004_membersmessage_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membersmessage',
            old_name='message',
            new_name='text',
        ),
    ]
