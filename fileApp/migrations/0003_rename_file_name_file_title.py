# Generated by Django 4.2.1 on 2023-05-17 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileApp', '0002_rename_title_file_file_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_name',
            new_name='title',
        ),
    ]