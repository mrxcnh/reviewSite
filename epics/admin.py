from django.contrib import admin
from epics.models import Epic


class EpicAdmin(admin.ModelAdmin):
    fields = list_display = [
        "title",
        "cover_img",
        "global_url",
    ]
    search_fields = ["title", "cover_img", "global_url"]

admin.site.register(Epic, EpicAdmin)