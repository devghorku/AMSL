from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from AMSL.serializers import EmployeePostSerializer, EmployeeSerializer, EmployeeCategorySerializer
from payroll.models import Payroll
from .models import Employee, EmployeeCategory
from AMSL.pagination import CustomPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['category', 'active']
    search_fields = ('name', 'employee_id',)
    ordering_fields = ('category',)
    ordering = ('-active')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return EmployeePostSerializer
        else:
            return EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        if not Payroll.objects.filter(employee_id=user_object.id).exists():
            Employee.objects.filter(pk=user_object.id).delete()
            user_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=False, methods=['GET'], name='get_all_employee')
    def all(self, request, *args, **kwargs):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'active',)
    ordering_fields = ('name',)
    ordering = ('-id')
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser, IsAuthenticated]

    @action(detail=False, methods=['GET'], name='get_all')
    def all(self, request, *args, **kwargs):
        queryset = EmployeeCategory.objects.all()
        serializer = EmployeeCategorySerializer(queryset, many=True)
        return Response(serializer.data)
