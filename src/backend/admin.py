from django.contrib import admin

# Register your models here.
from backend.models import TGUser, Message


@admin.register(TGUser)
class TGUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'date']
