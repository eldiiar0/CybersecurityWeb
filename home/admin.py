from django.contrib import admin

from .models import *


class HomePageAdmin(admin.ModelAdmin):
	list_display = ('title',)


class HomePageInfosAdmin(admin.ModelAdmin):
	list_display = ('title',)


class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','date', )


class EventsAdmin(admin.ModelAdmin):
	list_display = ('title','date',)


class AboutPageAdmin(admin.ModelAdmin):
	list_display = ('title',)

class AboutPageInfosAdmin(admin.ModelAdmin):
	list_display = ('title',)

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name',)


class ParentPageAdmin(admin.ModelAdmin):
	list_display = ('title', )

class ParentInfosAdmin(admin.ModelAdmin):
	list_display = ('title',)


class ChildrenPageAdmin(admin.ModelAdmin):
	list_display = ('title',)


class ChildrenPageInfosAdmin(admin.ModelAdmin):
	list_display = ('title',)


class SocialMediaUrlsAdmin(admin.ModelAdmin):
	list_display = ('instagram', 'facebook', 'twitter')


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(HomePageInfos, HomePageInfosAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(AboutPageInfos, AboutPageInfosAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(ParentPage, ParentPageAdmin)
admin.site.register(ParentPageInfos, ParentInfosAdmin)
admin.site.register(ChildrenPage, ChildrenPageAdmin)
admin.site.register(ChildrenPageInfos, ChildrenPageInfosAdmin)
admin.site.register(SocialMediaUrls, SocialMediaUrlsAdmin)
