from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscribe
from users.models import User


# Create your tests here.


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@user.com',
            password='password',
        )

        self.course = Course.objects.create(
            title='test course',
            description='description',
            owner=self.user,
        )

        self.lesson = Lesson.objects.create(
            title='test lesson',
            description='description',
            course=self.course,
            owner=self.user,
        )

        self.client.force_authenticate(user=self.user)

    def test_get_detail(self):

        response = self.client.get(
            reverse('courses:detail', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
                    response.json(),
            {
                        "id": self.lesson.pk,
                        "title": "test lesson",
                        "preview": None,
                        "description": "description",
                        "video_url": None,
                        "course": self.course.pk,
                        "owner": self.user.pk
                    }
                )

    def test_update(self):

        data = {
                    "title": "test update lesson",
                    "description": "update",
                    "video_url": 'https://www.youtube.com/watch?v=O4irXQhgMqg',
                    "course": self.course.pk,
                    "owner": self.user.pk
        }

        response = self.client.put(
            reverse('courses:update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
                    response.json(),
            {
                        "id": self.lesson.pk,
                        "title": "test update lesson",
                        "preview": None,
                        "description": "update",
                        "video_url": 'https://www.youtube.com/watch?v=O4irXQhgMqg',
                        "course": self.course.pk,
                        "owner": self.user.pk
                    }
                )

    def test_create_lesson(self):

        data = {
                    "title": 'test 2',
                    "description": 'description',
                    "video_url": 'https://www.youtube.com/watch?v=SiAuAJBZuGs',
                    "course": self.course.pk,
                    "owner": self.user.pk,
        }

        response = self.client.post(
            reverse('courses:create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )


    def test_create_delete_sub(self):

        data = {
                    "user": self.user.pk,
                    "course": self.course.pk,
        }

        response = self.client.post(
            reverse('courses:sub_create', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscribe.objects.all().count(),
            1
        )

        response = self.client.delete(
            reverse('courses:sub_delete', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Subscribe.objects.all().count(),
            0
        )

    def test_delete(self):

        response = self.client.delete(
            reverse('courses:delete', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
