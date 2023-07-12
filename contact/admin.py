from django.contrib import admin
from .models import Contact, Subscribe
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'message']
    date_hierarchy = 'created_date'
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']