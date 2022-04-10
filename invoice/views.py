from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from AMSL.serializers import InvoicePostSerializer, InvoiceSerializer, InvoiceItemSerializer
from .models import Invoice, InvoiceItem
from AMSL.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['invoice_date']
    search_fields = ('invoice_id',)
    ordering_fields = ('-id',)
    ordering = ('-invoice_id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return InvoicePostSerializer
        else:
            return InvoiceSerializer


class InvoiceItemsViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('-id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    @action(detail=False, methods=['GET'], name='get_all')
    def all(self, request, *args, **kwargs):
        queryset = InvoiceItem.objects.all()
        serializer = InvoiceItemSerializer(queryset, many=True)
        return Response(serializer.data)
