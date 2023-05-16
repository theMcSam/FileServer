# Generated by Django 4.2.1 on 2023-05-15 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('number_of_emails', models.IntegerField(default=0)),
                ('number_of_downloads', models.IntegerField(default=0)),
            ],
        ),
    ]
