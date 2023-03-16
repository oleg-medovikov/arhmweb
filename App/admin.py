from django.contrib import admin
from App.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'occupation']
    search_fields = ['name']
    list_per_page = 8

    class Meta:
        app_label = 'arhem_data'


admin.site.register(Employee, EmployeeAdmin)
