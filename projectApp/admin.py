from django.contrib import admin
from .models import project, part, completed_task


# Register your models here.

class projectModel(admin.ModelAdmin):
    list_display = ["__str__", "started_on", "ended_on"]
    list_per_page = 10
    list_filter = ["started_on", "ended_on"]
    search_fields = ["__str__"]

    class Meta:
        model = project


admin.site.register(project, projectModel)


class partModel(admin.ModelAdmin):
    list_display = ["__str__", "project", "worker"]
    list_per_page = 10
    list_filter = ["project"]
    search_fields = ["__str__", "project"]

    class Meta:
        model = part


admin.site.register(part, partModel)
