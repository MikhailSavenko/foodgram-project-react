from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Ingredient(models.Model):
    """Модель Ингредиента"""

    name = models.CharField(max_length=200, db_index=True)
    measurement_unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Модель Тэг"""

    name = models.CharField(max_length=30, blank=False, unique=True)
    color = models.CharField(
        max_length=20,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель Рецепт"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, related_name='recipes'
    )
    name = models.CharField(max_length=200, blank=False)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipeAmount',
        blank=False,
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag, blank=False, related_name='recipes_tags'
    )
    text = models.TextField(blank=False)
    cooking_time = models.IntegerField(blank=False, default=1,
                                       validators=[MinValueValidator(1)])
    image = models.ImageField(blank=False, upload_to='recipe_images/')
    created_at = models.DateTimeField(auto_now_add=True)


class IngredientRecipeAmount(models.Model):
    """Промежуточная модель связи Рецепта Ингредиента
    с добавлением количества"""

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredient_used'
    )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='recipe_used'
    )
    amount = models.IntegerField(
        blank=False, default=1, validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'], name='recipe_ingredient'
            )
        ]


class FavoriteRecipe(models.Model):
    """Модель избранное"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    """Модель список покупок"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
