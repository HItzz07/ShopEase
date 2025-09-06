from django.db import models
from companies.models import Company


class Customer(models.Model):
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="customers")
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class Bill(models.Model):
    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("ISSUED", "Issued"),
        ("PAID", "Paid"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="bills")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bills")
    bill_number = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['company', 'bill_number'], name='unique_company_bill_number')
        ]

    def __str__(self):
        return f"{self.bill_number} - {self.company.name}"

    def save(self, *args, **kwargs):
        if not self.bill_number:
            super().save(*args, **kwargs)
            self.bill_number = f"Bill-{self.id}"
            return super().save(update_fields=["bill_number"])

        super().save(*args, **kwargs)


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
