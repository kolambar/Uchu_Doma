from django.contrib import admin

from courses.models import Payments, Lesson, Course, Subscribe


# Register your models here.


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'summ_of_fee', 'way_of_pay', 'session_id', 'is_paid', )
    list_filter = ('way_of_pay', 'session_id', 'is_paid', )
    search_fields = ('user', 'date', 'summ_of_fee', 'session_id', 'is_paid', )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'course',)
    list_filter = ('course',)
    search_fields = ('title', 'description', 'video_url',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', )
    list_filter = ('course', 'user', )
    search_fields = ('user', 'course', )