# Generated by Django 4.2 on 2024-05-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
