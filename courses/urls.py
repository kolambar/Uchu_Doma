from django.urls import path
from rest_framework import routers

from courses.apps import CoursesConfig
from courses.views.course import CourseViewSet, SubscribeCreateView, SubscribeDeleteView
from courses.views.lesson import *
from courses.views.payments import PaymentsListView


app_name = CoursesConfig.name


urlpatterns = [
    path('', LessonListView.as_view(), name='list'),
    path('create/', LessonCreateView.as_view(), name='create'),
    path('<int:pk>/', LessonDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='delete'),

    path('payments_list/', PaymentsListView.as_view(), name='pay_list'),

    path('create/<int:pk>', SubscribeCreateView.as_view(), name='sub_create'),
    path('sub/<int:pk>/delete/', SubscribeDeleteView.as_view(), name='sub_delete'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
