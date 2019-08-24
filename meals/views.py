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
from meals.models import MealType, Meal, Food, MealPlan
from meals.serializers import MealTypeSerializer, MealSerializer, MealPlanSerializer, FoodSerializer
from meals.utils.meal_finder import get_matching_meals



logger = logging.getLogger(__name__)


class ReadOnlyMealAbstractViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Abstract Parent Readonly ViewSet
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
        logger.debug('Data: {0} | User: {1}'.format(self.request.data, self.request.user))
        queryset = self.queryset_class.objects.all()
        return queryset


class MealTypeViewSet(ReadOnlyMealAbstractViewSet):
    """
    handles ViewSet for MealType
    """
    serializer_class = MealTypeSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = MealType
    queryset = queryset_class.objects.none()


class FoodViewSet(ReadOnlyMealAbstractViewSet):
    """
    handles ViewSet for Food
    """
    serializer_class = FoodSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = Food
    queryset = queryset_class.objects.none()


class MealPlanViewSet(ReadOnlyMealAbstractViewSet):
    """
    handles ViewSet for Meal Plan
    """
    serializer_class = MealPlanSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = MealPlan
    queryset = queryset_class.objects.none()


class MealViewSet(ReadOnlyMealAbstractViewSet):
    """
    handles ViewSet for Meal
    """
    serializer_class = MealSerializer
    filter_fields = ['id', 'name', 'slug']
    search_fields = ['name', 'slug']
    queryset_class = Meal
    queryset = queryset_class.objects.none()

    @action(detail=False, methods=['get'])
    def free(self, request):
        """
        Sample URL: http://localhost:8000/api/meals/meal/free?food_ids=1,11
        :param request:
        :return:
        """
        logger.debug('Data: {0} | User: {1}'.format(self.request.data, self.request.user))

        food_ids = dict(request.query_params).get('food_ids', [''])[0].split(',')

        # todo: custom exception handler and middleware to parse it
        try:
            meal_ids = get_matching_meals(food_ids=food_ids)
        except ValueError as e:
            return Response({"errors": "Something went wrong: {0}".format(e.__str__())},
                            status=HTTP_400_BAD_REQUEST)

        return Response({"meal_ids": meal_ids})

