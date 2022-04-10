from rest_framework import routers
from expense.views import ExpenseViewSet, ExpenseCategoryViewSet
from income.views import IncomeViewSet, IncomeCategoryViewSet
from employee.views import EmployeeViewSet, EmployeeCategoryViewSet
from invoice.views import InvoiceViewSet, InvoiceItemsViewSet
from payroll.views import PayrollViewSet
# from stock.views import StockViewSet, ExportViewSet
# from unit.views import UnitViewSet
# from product.views import ProductViewSet
# from productType.views import ProductTypeViewSet

router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet)
router.register(r'expense-category', ExpenseCategoryViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'income-category', IncomeCategoryViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'employee-category', EmployeeCategoryViewSet)
router.register(r'invoice', InvoiceViewSet)
router.register(r'invoice-items', InvoiceItemsViewSet)
router.register(r'payroll', PayrollViewSet)
# router.register(r'product', ProductViewSet)
# router.register(r'product-type', ProductTypeViewSet)
# router.register(r'stock', StockViewSet)
# router.register(r'export', ExportViewSet)

