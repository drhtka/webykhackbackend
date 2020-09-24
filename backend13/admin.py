from django.contrib import admin
from backend13.models import CreateDb
# Register your models here.

class CreateDbAdmin(admin.ModelAdmin):
    list_display = ('id', 'tovarname', 'price', 'sale')
    list_filter = ('id', 'tovarname', 'price', 'sale')

admin.site.register(CreateDb, CreateDbAdmin)