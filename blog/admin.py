from django.contrib import admin
from blog.models import post , categories , comment
from django_summernote.admin import SummernoteModelAdmin


class postAdmin(SummernoteModelAdmin):
        date_hierarchy = "publish_date"
        empty_value_display = "-empty-"
        list_display = ["title" ,'author' , "count_views", "status", "publish_date" ,"login_require" ]
        search_fields = ["title" , 'content' , ]
        list_filter = ["status" , 'author' ,]
        summernote_fields = ('content',)
        
class comentAdmin(admin.ModelAdmin):
        date_hierarchy = "create_date"
        empty_value_display = "-empty-"
        list_display = ["name" ,'email' , "approved", "create_date" , ]
        search_fields = ["name" , 'content' , ]
        list_filter = ["approved" , 'email' ,]
        summernote_fields = ('message',)


admin.site.register(comment, comentAdmin)
admin.site.register(categories)
admin.site.register(post, postAdmin)
# Register your models here.
