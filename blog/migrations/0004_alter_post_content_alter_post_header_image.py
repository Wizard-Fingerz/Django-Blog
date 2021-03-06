# Generated by Django 4.0.3 on 2022-06-15 12:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='#', upload_to='header_images'),
        ),
    ]
