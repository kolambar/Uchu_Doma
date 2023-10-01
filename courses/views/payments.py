from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from courses.models import Payments
from courses.serializers.payments import PaymentsSerializer


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course', 'lesson', 'way_of_pay']
    ordering_fields = ['date']
