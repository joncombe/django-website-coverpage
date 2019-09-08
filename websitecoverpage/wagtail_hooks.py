from django.utils import timezone
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import WebsiteCoverPage


class WebsiteCoverPageAdmin(ModelAdmin):
    model = WebsiteCoverPage
    menu_icon = 'pick'
    add_to_settings_menu = True
    exclude_from_explorer = True
    list_display = ('name', 'start_datetime', 'end_datetime', 'date_status')
    search_fields = ('name',)

    def date_status(self, obj):
        now = timezone.now()

        if obj.start_datetime > obj.end_datetime:
            return 'INVALID DATES'
        elif obj.end_datetime <= now:
            return 'Past'
        elif obj.start_datetime > now:
            return 'Future'
        else:
            return 'Active'
    date_status.short_description = 'Status'

modeladmin_register(WebsiteCoverPageAdmin)