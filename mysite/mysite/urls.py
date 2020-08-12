"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?i)admin/', admin.site.urls),
    url(r'^(?i)getInfo', views.getInfo),
#     url(r'^getS3BucketFile$', views.getS3InfoFromFile),
#     url(r'^getS3BucketFiles$', views.getS3FileListWithBucket),
#     url(r'^getS3Files', views.getS3FileList),
#     url(r'^getS3File', views.getS3Info),
    url(r'^$', views.getInfo),
]
