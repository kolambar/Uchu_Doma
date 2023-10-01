from rest_framework import serializers

from courses.models import Payments


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'