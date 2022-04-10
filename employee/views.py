from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from AMSL.serializers import EmployeePostSerializer, EmployeeSerializer, EmployeeCategorySerializer
from .models import Employee, EmployeeCategory
from AMSL.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('category__name',)
    ordering_fields = ('category',)
    ordering = ('-category__id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return EmployeePostSerializer
        else:
            return EmployeeSerializer

    @action(detail=False, methods=['GET'], name='get_all_employee')
    def all(self, request, *args, **kwargs):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('-id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    @action(detail=False, methods=['GET'], name='get_all')


    def all(self, request, *args, **kwargs):
        queryset = EmployeeCategory.objects.all()
        serializer = EmployeeCategorySerializer(queryset, many=True)
        return Response(serializer.data)
