from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from courses.models import Course
from courses.permissions import IsStaffOrOwner, IsOwner, IsAuthenticatedNoStaff
from courses.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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
