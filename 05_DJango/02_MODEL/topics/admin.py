from django.contrib import admin
from .models import Topic
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'update_at',)

admin.site.register(Topic, TopicAdmin)