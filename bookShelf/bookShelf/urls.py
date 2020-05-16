"""bookShelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import RedirectView

from books import views

views.startup_function()

urlpatterns = [
    url(r'^accounts/login/$', RedirectView.as_view(url='/books/userlogin', permanent=True)),
    url(r'^books/', include('books.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^healthz$',RedirectView.as_view(url='/books/healthz/', permanent=True)),
    url(r'^$', RedirectView.as_view(url='/books/', permanent=True)),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

