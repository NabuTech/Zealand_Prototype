from django.contrib import admin
from .models import EmailAccount, Email, EmailFolder

@admin.register(EmailAccount)
class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'is_active')
    search_fields = ('email_address',)
    filter_horizontal = ('users_with_access',)  # Easier management of users with access

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'sent_at', 'is_read')
    search_fields = ('subject', 'body')

admin.site.register(EmailFolder)
