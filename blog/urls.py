import statistics
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from personal_portfolio import settings
from . import views

from django.urls import include

app_name = 'blog'
urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
   path('<int:blog_id>/',views.details, name='details')
]

