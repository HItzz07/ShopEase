from django.contrib import admin
from .models import Company
# ----- Company Admin -----
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    list_filter = ("owner",)
    search_fields = ("name", "owner__username")
