from django.contrib import admin
from .models import Contact,Feedback,Complaint

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','second_name','email_id','status','mobile_no')
    list_filter = ('first_name',)
    search_fields = ('id', 'first_name')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','farmer_name','email','title','details','date')
    list_filter = ('farmer_name',)
    search_fields = ('id', 'farmer_name')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','complaint_type','complaint_message')
    list_filter = ('name',)
    search_fields = ('id','complaint_type')

admin.site.register(Contact,ContactAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Complaint,ComplaintAdmin)

