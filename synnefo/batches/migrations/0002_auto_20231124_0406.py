# Generated by Django 3.2.12 on 2023-11-24 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='batch',
            new_name='bach',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='batch',
            new_name='bach',
        ),
    ]
