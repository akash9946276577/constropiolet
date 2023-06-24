from django.contrib import admin
from .models import Materials


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'quality')


# Register your models here.

admin.site.register(Materials, MaterialsAdmin)
