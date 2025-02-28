from django.contrib import admin
from .models import Item
from .models import StaffProfile
# Register your models here.
admin.site.register(Item)

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'phone_number')
    search_fields = ('user__username', 'department')
    