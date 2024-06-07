from django.contrib import admin

from .models import *

class MembersPageInfosAdmin(admin.ModelAdmin):
	list_display = ('title',)

class MembersNewsAdmin(admin.ModelAdmin):
	list_display = ('title','date', )


class MembersEventsAdmin(admin.ModelAdmin):
	list_display = ('title','date', )


class MembersResourcesAdmin(admin.ModelAdmin):
	list_display = ('title','date', )


class MembersMessagesAdmin(admin.ModelAdmin):
	list_display = ('title','date', )


admin.site.register(MembersPageInfos, MembersPageInfosAdmin)
admin.site.register(MembersMessage, MembersMessagesAdmin)
admin.site.register(MembersNews, MembersNewsAdmin)
admin.site.register(MembersEvents, MembersEventsAdmin)
admin.site.register(MembersResources, MembersResourcesAdmin)