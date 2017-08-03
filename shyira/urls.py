from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from service.views import Events,Contact,Gallery
urlpatterns = [
    # Examples
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/schedule/$', Events,name='events-schedule'),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^$',TemplateView.as_view(template_name="home.html")),
    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'^service/$',TemplateView.as_view(template_name="services.html"),name='service'),
    url(r'^gallery/$',Gallery, name='gallery'),
    url(r'^slider/$',TemplateView.as_view(template_name='thumbnail.html'), name='slider'),
    url(r'^show/$', TemplateView.as_view(template_name='slider.html'), name='slider'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)