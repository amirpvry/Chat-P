from django.contrib import admin
from .models import contact
class postAdmin(admin.ModelAdmin):
        date_hierarchy = "publish_date"
        empty_value_display = "-empty-"
        list_display = ["title" , "count_views", "status", "publish_date"]
        search_fields = ["title" , 'content' ]
        list_filter = ["status" , ]
admin.site.register(contact)
# Register your models here.
