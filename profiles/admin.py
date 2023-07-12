from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['author__username', 'author__first_name', 'author__last_name']


admin.site.register(Profile, ProfileAdmin)