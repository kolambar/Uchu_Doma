import stripe
from rest_framework.filters import SearchFilter, OrderingFilter
from courses.serializers.payments import PaymentsSerializer
from courses.services import get_payment, is_paid
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from courses.models import Payments, Course
import datetime

from users.models import User


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'lesson', 'way_of_pay']
    ordering_fields = ['date']


def page_with_pay_link(request, course_id, amount):

    course = Course.objects.get(pk=course_id)

    link = get_payment(course, amount)
    print(link)
    return HttpResponse(request, link)


def check_pay(request, course_pk):

    course = Course.objects.get(pk=course_pk)
    session = stripe.checkout.Session.retrieve(
        str(course_pk),
    )  # client_reference_id сессии был взят из pk курса

    user_email = session.customer_details['email']

    user = User.objects.get(email=user_email)

    if is_paid(session):
        Payments.objects.create(
            user=user,
            data=datetime.data.now(),
            course=course,
            summ_of_fee=session.amount_total,
            way_of_pay='bank_transfer'
        )

    return HttpResponse(request)
