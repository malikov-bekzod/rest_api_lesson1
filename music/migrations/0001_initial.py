# Generated by Django 5.0.4 on 2024-04-30 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.URLField(null=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.URLField(null=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.URLField(null=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('albom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.albom')),
            ],
        ),
    ]