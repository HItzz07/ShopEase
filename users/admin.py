# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



# User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # just add your extra field to list display and search
    list_display = UserAdmin.list_display + ("contact_number",)
    search_fields = UserAdmin.search_fields + ("contact_number",)

    # extend the default fieldsets to include contact_number
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("contact_number",)}),
    )

    # extend add_fieldsets to include contact_number when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("contact_number",)}),
    )

# # ----- Custom User Admin -----
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ("username", "email", "contact_number", "is_staff", "is_active")
#     list_filter = ("is_staff", "is_active")
#     fieldsets = (
#         (None, {"fields": ("username", "email", "contact_number", "password")}),
#         ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("username", "email", "contact_number", "password1", "password2", "is_staff", "is_active")}
#         ),
#     )
#     search_fields = ("email", "username", "contact_number")
#     ordering = ("username",)