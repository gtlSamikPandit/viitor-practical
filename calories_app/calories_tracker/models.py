from django_extensions.db.models import TimeStampedModel
from django.db import models


class FoodItem(TimeStampedModel):
    food_name = models.CharField('Food Name', max_length=20)
    calories = models.DecimalField('Calories', decimal_places=2, max_digits=5, default=0)
    protein = models.DecimalField('Protein', decimal_places=2, max_digits=5, default=0)
    fat = models.DecimalField('Fat',decimal_places=2, max_digits=5, default=0)

    def __str__(self):
        return "%s | %s" % (self.id, self.food_name)

    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"


class UserFood(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    food = models.ForeignKey('FoodItem', on_delete=models.CASCADE)
