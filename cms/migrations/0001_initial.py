# Generated by Django 5.1.1 on 2024-10-04 08:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_image', models.ImageField(blank=True, null=True, upload_to='latest_images/')),
                ('popular_image', models.ImageField(blank=True, null=True, upload_to='popular_images/')),
                ('subscribe_image', models.ImageField(blank=True, null=True, upload_to='subscribe_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('science', 'Science'), ('technology', 'Technology'), ('politics', 'Politics'), ('sports', 'Sports'), ('space', 'Space'), ('economy', 'Economy')], max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
