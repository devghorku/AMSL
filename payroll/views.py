from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from AMSL.serializers import PayrollPostSerializer, PayrollSerializer
from .models import Payroll
from AMSL.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('employee__name',)
    ordering_fields = ('employee',)
    ordering = ('-employee__id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return PayrollPostSerializer
        else:
            return PayrollSerializer

