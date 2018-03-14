
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog import views as uploader_view
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home , name='home'),
    url(r'^mythoughts/$', views.mythoughts , name = "mythoughts"),
    url(r'^readarticle/(?P<pk>\d+)/$', views.readarticle, name='readarticle'),
    url(r'^base/$', views.base , name='base'),
    url(r'^author_info/$', uploader_view.author_info , name='author_info'),
    url(r'^readarticle/$', views.readarticle , name = "readarticle" ),
    url(r'^martor/', include('martor.urls')),
    url(r'^signup/$', accounts_views.signup , name = "signup" ),
    url(r'^archive/$', views.archive , name = "archive" )
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
