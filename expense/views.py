from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from AMSL.serializers import ExpensePostSerializer, ExpenseSerializer, ExpenseCategorySerializer
from .models import Expense, ExpenseCategory
from AMSL.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('category__name',)
    ordering_fields = ('category',)
    ordering = ('-category__id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return ExpensePostSerializer
        else:
            return ExpenseSerializer


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('-id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    @action(detail=False, methods=['GET'], name='get_all')


    def all(self, request, *args, **kwargs):
        queryset = ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(queryset, many=True)
        return Response(serializer.data)
