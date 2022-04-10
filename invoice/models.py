from django.db import models


# Create your models here.
class Invoice(models.Model):
    invoice_id = models.CharField(unique=True, max_length=50)
    invoice_date = models.DateTimeField()
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    client_name = models.CharField(max_length=250)
    client_address = models.TextField(null=True, blank=True)
    vat = models.FloatField(default=0)
    due = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.invoice_id


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField()
    base = models.CharField(null=True, blank=True, max_length=10)
    unit_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

