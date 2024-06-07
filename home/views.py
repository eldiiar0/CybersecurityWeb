from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.


def home_page(request):
	home_info = HomePage.objects.all()
	main_info = HomePageInfos.objects.all()
	news = News.objects.all()
	events = Events.objects.all()
	socials = SocialMediaUrls.objects.all()
	print(main_info.first)
	return render(request, 'home/home_page.html',{'home_info': home_info,
		'news':news, 'events': events, 'socials':socials, 'main_info':main_info})


def one_news(request, id):
	one_news = get_object_or_404(News, pk=id)
	return render(request, 'home/one_news.html',{'one_news': one_news})


def one_event(request, id):
	one_event = get_object_or_404(Events, pk=id)
	return render(request, 'home/one_event.html',{'one_event': one_event})


def about(request):
	about_info = AboutPage.objects.all()
	main_info = AboutPageInfos.objects.all()
	partners = Partner.objects.all()
	return render(request, 'about.html', {'about_info': about_info, 'partners': partners, 'main_info':main_info})


def for_parents(request):
	parents_info = ParentPage.objects.all()
	main_info = ParentPageInfos.objects.all()
	return render(request, 'for-parents.html', {'parents_info': parents_info, 'main_info':main_info})


def for_children(request):
	children_info = ChildrenPage.objects.all()
	main_info = ChildrenPageInfos.objects.all()
	return render(request, 'for-children.html', {'children_info': children_info, 'main_info':main_info})



