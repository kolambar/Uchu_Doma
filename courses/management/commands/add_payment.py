from django.core.management.base import BaseCommand

from courses.models import Payments, Course, Lesson
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments = Payments.objects.bulk_create([
            Payments(
                user=User.objects.get(pk=2),
                date='2023-09-02',
                course=Course.objects.get(pk=3),
                summ_of_fee=2000,
                way_of_pay='bank_transfer'
            ),
            Payments(
                user=User.objects.get(pk=3),
                date='2023-10-01',
                lesson=Course.objects.get(pk=3),
                summ_of_fee=3000,
                way_of_pay='cash'
            )
        ])
