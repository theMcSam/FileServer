# Generated by Django 4.2.1 on 2023-05-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='title',
            new_name='file_name',
        ),
    ]