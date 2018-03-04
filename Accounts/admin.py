from django.contrib import admin
from .models import Staff, Salary_info, Bank_statement


# Register your models here.
class stuffModel(admin.ModelAdmin):
    list_display = ["__str__", "rank", "phone", "joined"]
    list_per_page = 10
    list_filter = ["rank", "joined"]
    search_fields = ["__str__", "rank", "joined"]

    class Meta:
        model = Staff

admin.site.register(Staff, stuffModel)


class salaryModel(admin.ModelAdmin):
    list_display = ["__str__", "monthly_salary", "total_salary", "paid"]
    list_per_page = 10
    list_filter = ["monthly_salary"]
    search_fields = ["__str__", "monthly_salary"]

    class Meta:
        model = Salary_info

admin.site.register(Salary_info, salaryModel)


class bank_stmtModel(admin.ModelAdmin):
    list_display = ["__str__", "ac_no", "bank_name", "branch"]
    list_per_page = 10
    list_filter = ["bank_name", "branch"]
    search_fields = ["__str__", "branch", "bank_name", "ac_no"]

    class Meta:
        model = Bank_statement

admin.site.register(Bank_statement, bank_stmtModel)
