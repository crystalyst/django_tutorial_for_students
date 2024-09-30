from django.contrib import admin

# from . import models
from .models import User, Tweet, Like

# admin.site.register(models.User)
# admin.site.register(models.Tweet)
# admin.site.register(models.Like)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "user", "created_at", "updated_at", "like_count")

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = "Number of Likes"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
