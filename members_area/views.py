from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


from .models import *
from .forms import *


@login_required
def member_page(request):
	form = MessageForm()
	main_info = MembersPageInfos.objects.all()
	member_news = MembersNews.objects.all()
	member_events = MembersEvents.objects.all()
	resources = MembersResources.objects.all()
	context = {'m_news':member_news, 'm_events': member_events, 'resources':resources,
				'message_form': form,'main_info':main_info}
	# return render(request, 'members_area/member_page.html',context)

	if request.method == 'POST': # If the form has been submitted...
		form = MessageForm(request.POST) # A form bound to the POST data
		if form.is_valid():# All validation rules pass
			data = form.cleaned_data
			member_msg = MembersMessage(title=data['title'],text=data['text'])
			member_msg.save()
			messages.success(request, 'Your message has been sent!')
			return redirect('members_area:member_page')
	else:
		return render(request, 'members_area/member_page.html',context)


@login_required
def one_news(request, id):
	one_news = get_object_or_404(MembersNews, pk=id)
	return render(request, 'members_area/one_news.html',{'one_news': one_news})


@login_required
def one_event(request, id):
	one_event = get_object_or_404(MembersEvents, pk=id)
	return render(request, 'members_area/one_event.html',{'one_event': one_event})


@login_required
def download_file(request, file_id):
	get_file = get_object_or_404(MembersResources, pk=file_id)
	file_path = get_file.files.path
	filename_extension = 1
	response = FileResponse(get_file.files, as_attachment=True, )
	return response

