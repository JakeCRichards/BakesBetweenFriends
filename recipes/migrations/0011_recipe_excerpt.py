# Generated by Django 4.2.19 on 2025-03-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_baker_profile_pic_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='excerpt',
            field=models.TextField(default=''),
        ),
    ]
