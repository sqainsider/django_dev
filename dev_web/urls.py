"""dev_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from api.models import MovieResource
from api.models import *
from . import views

# Upload Files
from django.conf import settings
from django.conf.urls.static import static


# APi Testypie framework
movie_resource = MovieResource()
country_resource = CountryResource()
book_resource = BookResource()


# movie_resource.urls

urlpatterns = [
    # path('/', home),

    # Admin
    path('admin/', admin.site.urls),

    path('', include('common.urls')),

    # User Account
    path('users/', include('django.contrib.auth.urls')),


    # tastypie APIs framework
    path('examples/api/', include(movie_resource.urls)),
    path('examples/api/', include(country_resource.urls)),
    path('examples/api/', include(book_resource.urls)),


    # django restful api framework
    # path('examples/api/rest/', include('api.urls')),
    # path('examples/api/rest/', include('todos.urls')),
    # path('examples/api/rest/', include('apiRest.urls')),



    # new APPs
    # Examples
    path('examples/movies/', include('movies.urls')),
    path('examples/blog/', include('blog.urls')),
    path('examples/books/', include('books.urls')),
    path('examples/hello/', include('hello.urls')),
    path('examples/uploadfile/', include('media.urls')),


    path('splunk/', include('splunk.urls')),


]

# Upload Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
