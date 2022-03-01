from django.contrib import admin
from .models import TableRows


@admin.register(TableRows)
class TableRowsAdmin(admin.ModelAdmin):
    pass
