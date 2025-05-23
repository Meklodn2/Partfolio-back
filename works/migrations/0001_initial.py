# Generated by Django 5.1.6 on 2025-03-13 05:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('work_image', models.ImageField(upload_to='works/')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(related_name='works', to='tags.tag')),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
                'ordering': ['-date_posted'],
            },
        ),
    ]
