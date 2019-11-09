from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('registration/', views.registration, name = 'registration'),
	path('profile/', views.menu, name = 'menu'),
	path('', views.home_page, name = 'home_page')
]

urlpatterns += staticfiles_urlpatterns()