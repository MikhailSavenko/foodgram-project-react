# Generated by Django 4.2.4 on 2023-09-15 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0002_alter_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='shopping_recipe',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shopping_recipe',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.recipe',
            ),
            preserve_default=False,
        ),
    ]
