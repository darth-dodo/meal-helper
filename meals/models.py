# third party imports

# django imports
from django.db import models
from django.core.validators import MinValueValidator

# project level imports
from utils.model_utils import AbstractRowInformation, AbstractNameAndDescription, custom_slugify

# app level imports


class MealType(AbstractRowInformation, AbstractNameAndDescription):
    """

    """

    _MODEL_CODE = 'MT'

    class Meta:
        db_table = 'meal_types'

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(MealType, cls).from_db(db, field_names, values)
        # cache existing value
        new._updated_name = values[field_names.index('name')]
        return new

    def save(self, *args, **kwargs):
        new_meal_type = True if not self.pk else False

        # name related operations
        if new_meal_type or hasattr(self, '_updated_name'):
            self.slug = custom_slugify(self.name)

        super(MealType, self).save(*args, **kwargs)

    def __str__(self):
        return super().__str__()


class Meal(AbstractRowInformation, AbstractNameAndDescription):
    """

    """
    meal_type = models.ForeignKey(to='meals.MealType', related_name='meals', on_delete=models.PROTECT)
    foods = models.ManyToManyField(to='meals.Food', related_name='food_meals')
    tags = models.ManyToManyField(to='utils.Tag', related_name='tagged_meals', blank=True)

    _MODEL_CODE = 'ML'

    class Meta:
        db_table = 'meals'

    # explicit is better than implicit
    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(Meal, cls).from_db(db, field_names, values)
        # cache existing value
        new._updated_name = values[field_names.index('name')]
        return new

    def save(self, *args, **kwargs):
        new_meal = True if not self.pk else False

        # name related operations
        if new_meal or hasattr(self, '_updated_name'):
            self.slug = custom_slugify(self.name)

        super(Meal, self).save(*args, **kwargs)

    def __str__(self):
        return '{0}/{1}'.format(self.meal_type.__str__(), super().__str__())


class Food(AbstractRowInformation, AbstractNameAndDescription):
    """

    """
    calories = models.PositiveIntegerField(default=0)  # positive integer field allows zero
    tags = models.ManyToManyField(to='utils.Tag', related_name='tagged_food', blank=True)

    _MODEL_CODE = 'FD'

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(Food, cls).from_db(db, field_names, values)
        # cache existing value
        new._updated_name = values[field_names.index('name')]
        return new

    class Meta:
        db_table = 'foods'

    def save(self, *args, **kwargs):
        new_food = True if not self.pk else False

        # name related operations
        if new_food or hasattr(self, '_updated_name'):
            self.slug = custom_slugify(self.name)

        super(Food, self).save(*args, **kwargs)


class NutritionalInformation(AbstractRowInformation):
    """

    """
    carbs = models.FloatField(validators=[MinValueValidator(limit_value=0)], default=0)
    fats = models.FloatField(validators=[MinValueValidator(limit_value=0)], default=0)
    protein = models.FloatField(validators=[MinValueValidator(limit_value=0)], default=0)
    food = models.OneToOneField(to='meals.Food', on_delete=models.PROTECT)

    class Meta:
        db_table = 'nutritional_informations'

    def save(self, *args, **kwargs):
        super(NutritionalInformation, self).save(*args, **kwargs)


class MealPlan(AbstractRowInformation, AbstractNameAndDescription):
    """

    """
    meals = models.ManyToManyField(to='meals.Meal', related_name='meal_plans')

    _MODEL_CODE = 'MP'

    class Meta:
        db_table = 'meal_plans'

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(MealPlan, cls).from_db(db, field_names, values)
        # cache existing value
        new._updated_name = values[field_names.index('name')]
        return new

    def save(self, *args, **kwargs):
        new_meal_plan = True if not self.pk else False

        # name related operations
        if new_meal_plan or hasattr(self, '_updated_name'):
            self.slug = custom_slugify(self.name)

        super(MealPlan, self).save(*args, **kwargs)
