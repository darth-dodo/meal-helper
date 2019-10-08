# third party
import logging

# framework level libraries
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

# project level imports
from utils.views_utils import eager_load
from utils.pagination import MealPlannerPagination

# app level imports
from meals.models import MealType, Meal, Recipe, MealPlan
from meals.serializers import MealTypeSerializer, MealSerializer, MealPlanSerializer, RecipeSerializer
from meals.filters import MealFilter


logger = logging.getLogger(__name__)


class ReadOnlyMealAbstractViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Abstract Parent Readonly ViewSet for Meal App
    """
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset_class = None
    queryset = None
    serializer_class = None
    search_fields = []

    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = []
    ordering_fields = []
    ordering = ['id']

    pagination_class = MealPlannerPagination

    class Meta:
        abstract = True

    @eager_load
    def get_queryset(self):
        """
        Eager Loading the queryset by using a decorator which checks out `_SELECT_RELATED_FIELDS` AND
        `PREFETCH_RELATED_FIELD` defined on the serializer level to prevent N + 1 queries
        :return: queryset object
        """
        logger.debug('Data: {0} | User: {1}'.format(self.request.data, self.request.user))
        queryset = self.queryset_class.objects.all()
        return queryset


class MealTypeViewSet(ReadOnlyMealAbstractViewSet):
    """
    ReadOnly ModelViewSet for MealType
    """
    serializer_class = MealTypeSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = MealType
    queryset = queryset_class.objects.none()


class RecipeViewSet(ReadOnlyMealAbstractViewSet):
    """
    ReadOnly ModelViewSet for Recipe
    """
    serializer_class = RecipeSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = Recipe
    queryset = queryset_class.objects.none()


class MealPlanViewSet(ReadOnlyMealAbstractViewSet):
    """
    ReadOnly ModelViewSet for MealPlan
    """
    serializer_class = MealPlanSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = MealPlan
    queryset = queryset_class.objects.none()


class MealViewSet(ReadOnlyMealAbstractViewSet):
    """
    ReadOnly ModelViewSet for Meal

    `with_recipe` filter fetches all the Meals which are present in all of the recipes passed as query param
    Sample URL: https://meal-planner-hm.herokuapp.com/api/meals/meal/?with_recipe=2%2C4

    `free` action is used to parse data through task 1 and fetch the relevant meal ids
    Sample URL: https://meal-planner-hm.herokuapp.com/api/meals/meal/free?recipe_ids=1,11
    """
    serializer_class = MealSerializer
    filter_class = MealFilter
    search_fields = ['name', 'slug']
    queryset_class = Meal
    queryset = queryset_class.objects.none()
