from django.contrib import admin

# from . import models
from .models import User, Tweet, Like

# admin.site.register(models.User)
# admin.site.register(models.Tweet)
# admin.site.register(models.Like)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("contains", "Contains Elon Musk"),
            ("not_contains", "Does Not Contain Elon Musk"),
        )

    def queryset(self, request, queryset):
        if self.value() == "contains":
            return queryset.filter(payload__icontains="elon musk")
        if self.value() == "not_contains":
            return queryset.exclude(payload__icontains="elon musk")
        return queryset


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "user", "created_at", "updated_at", "like_count")
    search_fields = ("payload", "user__name")
    list_filter = ("created_at", ElonMuskFilter)

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = "Number of Likes"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ("user__name",)
    list_filter = ("created_at",)
