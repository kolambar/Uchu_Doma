from django.utils import inspect
from django.utils.functional import cached_property
from django.utils.inspect import method_has_no_args
from rest_framework.pagination import PageNumberPagination


class EducationalPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице
