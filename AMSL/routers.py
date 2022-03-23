from rest_framework import routers
from expense.views import ExpenseViewSet, ExpenseCategoryViewSet
# from stock.views import StockViewSet, ExportViewSet
# from unit.views import UnitViewSet
# from product.views import ProductViewSet
# from productType.views import ProductTypeViewSet

router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet)
router.register(r'expense-category', ExpenseCategoryViewSet)
# router.register(r'product', ProductViewSet)
# router.register(r'product-type', ProductTypeViewSet)
# router.register(r'stock', StockViewSet)
# router.register(r'export', ExportViewSet)

