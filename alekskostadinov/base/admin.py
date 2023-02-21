from django.contrib import admin

from base.models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass
