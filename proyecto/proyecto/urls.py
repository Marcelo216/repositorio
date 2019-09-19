from django.conf.urls import patterns, include, url
from aplicacion import views 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/',views.listarPersona),
    url(r'^compras/',views.listarCompra),
    url(r'^productos/',views.listarProducto),
)
