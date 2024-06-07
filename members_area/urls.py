from django.urls import path

from .views import *


app_name = 'members_area'
urlpatterns = [
    path('membersarea', member_page, name='member_page'),
    path('membersarea/news/<int:id>/', one_news, name='one_news'),
    path('membersarea/events/<int:id>/', one_event, name='one_event'),
    path('membersarea/download/<int:file_id>',download_file, name='download_file')
    
]
