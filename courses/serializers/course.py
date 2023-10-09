from rest_framework import serializers

from courses.models import Course, Lesson, Subscribe
from courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

    num_of_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribe(self, instance):
        request = self.context.get('request')
        user = request.user if request else None
        if user.is_authenticated:
            is_subscribe = 'не подписан'
            subscriptions = Subscribe.objects.filter(course=instance)
            for sub in subscriptions:
                if user == sub.user:
                    is_subscribe = 'подписан'
                    return is_subscribe
        else:
            is_subscribe = 'не авторизован'
        return is_subscribe

    def get_num_of_lesson(self, instance):
        return instance.lesson_set.count()


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__'
