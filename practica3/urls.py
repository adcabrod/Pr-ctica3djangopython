"""practica3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from posts.views import home, blogsView, PostView,  blogDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^blogs/$', blogsView.as_view()),
    url(r'posts/(?P<username>\w+)/$', blogDetailView.as_view()),
    url(r'posts/(?P<username>\w+)/(?P<pk>[0-9]+)$$', PostView.as_view()),
]
