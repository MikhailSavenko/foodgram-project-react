# Generated by Django 4.2.4 on 2023-08-30 13:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_ingredients_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipeamount',
            name='amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
