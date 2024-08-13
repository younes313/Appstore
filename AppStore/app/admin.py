from django.contrib import admin

from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_verified')
    list_filter = ('is_verified',)


admin.site.register(App, AppAdmin)
