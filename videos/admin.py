from django.contrib import admin
from .models import Video, Comment
from .metrics import get_most_commented_video
from django.utils.html import format_html


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'comment_count')
    readonly_fields = ['engagement_stats', 'created_at']

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comment count'

    def engagement_stats(self, obj=None):
        most = get_most_commented_video()
        if most:
            return format_html(
                "<b>Most Commented Video:</b><br><i>{}</i><br>Comments: {}",
                most.title,
                most.comments.count()
            )
        return "No videos available."

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'created_at')
        }),
        ('📊 Engagement Stats (read-only)', {
            'fields': ('engagement_stats',),
        }),
    )


admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)