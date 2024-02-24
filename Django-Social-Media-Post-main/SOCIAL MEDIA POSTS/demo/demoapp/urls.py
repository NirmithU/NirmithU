
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns=[
    path('',home,name="home"),
    path('add-comment/<id>',add_comment,name="add_comment"),
    path('delete-comment/<id>',delete_comment,name="delete_comment"),
    path('like-post/<id>',like_post,name="like_post"),
    path('hide-post/<id>',hide_post,name="hide_post"),
    path('delete-post/<id>',delete_post,name="delete_post"),
    path('post',your_post,name="post"),
    path('action-post/<id>',action_post,name="action_post"),
    path('add-post/',add_post,name="add_post"),

    # account
    path('login',handle_login,name='login'),
    path('signup',handle_signup,name='signup'),
    path('logout',handle_logout,name='logout'),
    path('profile',user_profile,name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)