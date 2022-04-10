from django.contrib import admin

# Register your models here.

from django.contrib import admin
from income.models import Income, IncomeCategory
# Register your models here.
admin.site.register(Income)
admin.site.register(IncomeCategory)