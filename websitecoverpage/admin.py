from django.contrib import admin
from websitecoverpage.models import WebsiteCoverPage

class WebsiteCoverPageAdmin(admin.ModelAdmin):
    pass

admin.site.register(WebsiteCoverPage, WebsiteCoverPageAdmin)