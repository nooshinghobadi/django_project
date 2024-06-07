from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from firstblog.views import home
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from firstblog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('firstblog.urls',namespace='blog')),
    path('account/', include('account.urls',namespace='account')),
    path('', home),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
           name='django.contrib.sitemaps.views.sitemap'),
    path('images/', include('images.urls',namespace='images')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)