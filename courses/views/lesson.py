from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from courses.models import Lesson
from courses.pagination import EducationalPagination
from courses.permissions import IsStaffOrOwner, IsOwner, IsAuthenticatedNoStaff
from courses.serializers.lesson import LessonSerializer



class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaffOrOwner]


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsStaffOrOwner]
    pagination_class = EducationalPagination

    def get_queryset(self):
        user = self.request.user
        if user.id:
            if user.is_staff:
                return Lesson.objects.all()
            else:
                return Lesson.objects.filter(owner=user)


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedNoStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaffOrOwner]


class LessonDeleteView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]
