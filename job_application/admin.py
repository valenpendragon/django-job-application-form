from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "occupation", "date")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("last_name", "first_name")


admin.site.register(Form, FormAdmin)
