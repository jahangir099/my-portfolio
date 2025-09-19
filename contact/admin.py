from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    

    change_list_template = "contact/contact_messages_list.html" 