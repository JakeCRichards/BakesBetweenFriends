# Generated by Django 4.2.19 on 2025-03-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['tag_name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='recipes',
            field=models.ManyToManyField(blank=True, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag_type',
            field=models.CharField(choices=[('dietary', 'Dietary'), ('allergy', 'Allergy'), ('cuisine', 'Cuisine')], max_length=50),
        ),
    ]
