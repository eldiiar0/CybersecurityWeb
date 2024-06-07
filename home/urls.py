from django.urls import path

from .views import *


app_name = 'home'
urlpatterns = [
    path('', home_page, name="home_page"),
    path('for_parents/', for_parents, name="for_parents"),
    path('for_children/', for_children, name="for_children"),
    path('about/', about, name="about"),
    path('news/<int:id>/', one_news, name='one_news'),
    path('events/<int:id>/', one_event, name='one_event')
]
