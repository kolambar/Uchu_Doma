from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Subscribe
from courses.pagination import EducationalPagination
from courses.permissions import IsStaffOrOwner, IsOwner, IsAuthenticatedNoStaff
from courses.serializers.course import CourseSerializer, SubscribeSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = EducationalPagination

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update']:
            permission_classes = [IsStaffOrOwner]
        elif self.action in ['destroy']:
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticatedNoStaff]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.id:
            if user.is_staff:
                return Course.objects.all()
            else:
                return Course.objects.filter(owner=user)


class SubscribeCreateView(CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def perform_create(self, serializer, *args, **kwargs):
        new_sub = serializer.save()
        new_sub.user = self.request.user
        pk = self.kwargs.get('pk')
        new_sub.course = Course.objects.get(pk=pk)
        new_sub.save()


class SubscribeDeleteView(DestroyAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


