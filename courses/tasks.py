from celery import shared_task
from django.core.mail import send_mail

from config import settings
from courses.models import Subscribe

from users.models import User
from datetime import datetime, timedelta


@shared_task
def report_an_update(course):
    subscribes = Subscribe.objects.filter(course=course)
    if subscribes:
        subject = f'{course.title} обновлен'
        message = 'Много интересного контента ждет вас'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = []

        for sub in list(subscribes):
            recipient_list.append(sub.user.email)

        send_mail(subject, message, from_email, recipient_list)


@shared_task
def check_is_active():
    three_months = datetime.now() - timedelta(days=90)
    User.objects.filter(last_login__lt=three_months).update(is_active=False)
