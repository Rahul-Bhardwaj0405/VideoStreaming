from django.contrib import admin
from .models import User, Video

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "password")

class VideoAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "video_url")


admin.site.register(User, UserAdmin)
admin.site.register(Video, VideoAdmin)
