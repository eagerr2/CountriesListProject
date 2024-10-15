from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index.html', views.index, name='index'),
	path('search/', views.search_feature, name='search-view')
]