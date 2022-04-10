from django.contrib.auth import get_user_model
from rest_framework import serializers
from expense.models import Expense, ExpenseCategory
from income.models import Income, IncomeCategory
from employee.models import EmployeeCategory, Employee
from payroll.models import Payroll
from invoice.models import InvoiceItem, Invoice


# from product.models import Product
# from productType.models import ProductType
# from stock.models import Export, Stock
# from unit.models import Unit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 'groups', 'password', 'is_active', 'is_staff',
            'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True}
        }


#
class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer()

    class Meta:
        model = Expense
        fields = '__all__'


class ExpensePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


# Income Serializer
class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer()

    class Meta:
        model = Income
        fields = '__all__'


class IncomePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


# employee serializer
class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    category = EmployeeCategorySerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Payroll
        fields = '__all__'


class PayrollPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('product_name', 'description', 'quantity', 'base', 'unit_price')


class InvoiceSerializer(serializers.ModelSerializer):
    invoice = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoicePostSerializer(serializers.ModelSerializer):
    invoices = InvoiceItemSerializer(many=True, write_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        invoice_data = validated_data.pop('invoices', [])
        invoice = Invoice.objects.create(**validated_data)
        for item in invoice_data:
            item['invoice'] = invoice
            InvoiceItem.objects.create(**item)
        return invoice

# class ProductTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductType
#         fields = '__all__'
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     unit = UnitSerializer()
#     product_type = ProductTypeSerializer()
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ProductPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class StockSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()
#
#     class Meta:
#         model = Stock
#         fields = '__all__'
#
#
# class StockPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         fields = '__all__'
#
#
# class ExportSerializer(serializers.ModelSerializer):
#     stock = StockSerializer()
#     product = ProductSerializer()
#
#     class Meta:
#         model = Export
#         fields = '__all__'
#
#
# class ExportPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Export
#         fields = '__all__'
