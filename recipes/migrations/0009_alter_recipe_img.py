# Generated by Django 4.1 on 2022-08-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(null=True, upload_to='recipe'),
        ),
    ]
