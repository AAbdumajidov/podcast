# Generated by Django 4.1.6 on 2023-02-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
