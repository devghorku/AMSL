from django.contrib.auth import get_user_model
from rest_framework import serializers
from expense.models import Expense, ExpenseCategory


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
