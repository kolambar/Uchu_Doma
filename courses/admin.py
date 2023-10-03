from django.contrib import admin

from courses.models import Payments, Lesson, Course


# Register your models here.


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'lesson', 'summ_of_fee', 'way_of_pay',)
    list_filter = ('way_of_pay',)
    search_fields = ('user', 'date', 'summ_of_fee',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'course',)
    list_filter = ('course',)
    search_fields = ('title', 'description', 'video_url',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)