from django.contrib import admin
from . models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter = ["owner", "order_status",]
    search_fields = ["owner", "order_id",]
admin.site.register(Order, OrderAdmin)
