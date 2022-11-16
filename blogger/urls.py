from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('hom', views.home, name='home'),
    path('contact', views.contact),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.user_signup, name='signup'),
    path('blog', views.add_blog, name='blog'),
    path('delete_blog/<id>', views.delete_blog),
    path('delete_blog_dash/<id>', views.delete_blog_dash),
    path('edit_blog/<id>', views.edit_blog),
    path('dashboard', views.dashboard, name='dashboard'),
    path('setcookie', views.cookie),
    path('getcookie', views.getcookie),
    path('delcookie', views.delcookie),
    path('setsession', views.setsession),
    path('getsession', views.getsession),
    path('delsession', views.delcookie),
]