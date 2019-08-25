from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


from utils.constants import MAX_PAGINATION_LIMIT, DEFAULT_PAGINATION_LIMIT, PAGE_SIZE


class MealPlannerPagination(LimitOffsetPagination):
    max_limit = MAX_PAGINATION_LIMIT
    default_limit = DEFAULT_PAGINATION_LIMIT
