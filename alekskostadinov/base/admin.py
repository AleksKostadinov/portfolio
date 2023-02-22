from django.contrib import admin

from base.models import Work, Certificate


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass

