# Generated by Django 4.2.1 on 2023-05-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file_size', models.CharField()),
                ('file_bytes', models.EmailField(max_length=254)),
            ],
        ),
    ]
