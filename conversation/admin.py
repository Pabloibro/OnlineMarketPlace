from django.contrib import admin
from .models import ConversationMessage, Conservation

# Register your models here.
admin.site.register(ConversationMessage)
admin.site.register(Conservation)