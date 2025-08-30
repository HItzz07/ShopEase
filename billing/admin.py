from django.contrib import admin
from .models import Customer, Bill, BillItem


# ---------------- Customer Admin ----------------
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "phone")  # match actual model fields
    search_fields = ("name", "email", "phone", "company__name")
    list_filter = ("company",)


# ---------------- Bill Admin ----------------
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("bill_number", "company", "customer", "date", "total_amount", "status")
    search_fields = ("bill_number", "customer__name", "company__name")
    list_filter = ("status", "company", "date")


# ---------------- BillItem Admin ----------------
@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ("description", "bill", "quantity", "unit_price", "line_total")
    search_fields = ("description", "bill__bill_number", "bill__customer__name")
    list_filter = ("bill__company",)

    # optional: make line_total read-only in admin
    readonly_fields = ("line_total",)

    # recalculate line_total automatically in admin save
    def save_model(self, request, obj, form, change):
        obj.line_total = obj.quantity * obj.unit_price
        super().save_model(request, obj, form, change)
