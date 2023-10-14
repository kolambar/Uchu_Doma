import stripe
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

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


@api_view(['GET'])
def page_with_pay_link(request, course_id, amount):

    course = Course.objects.get(pk=course_id)

    session = get_payment(course, amount)
    link = session.url

    Payments.objects.create(
        user=request.user,
        date=datetime.datetime.now().date(),
        course=course,
        summ_of_fee=session.amount_total,
        way_of_pay='bank_transfer',
        session_id=session.id,
        is_paid=False
    )

    return Response({"payment_link": link})


@api_view(['GET'])
def check_pay(request, course_pk):

    course = Course.objects.get(pk=course_pk)
    payment = Payments.objects.get(course=course, user=request.user)

    session = stripe.checkout.Session.retrieve(
        payment.session_id,
    )

    if is_paid(session):
        payment.is_paid = True
        payment.save()

        return Response({"status": "paid"})

    return Response({"status": "Error of payment. Please call for support"})
