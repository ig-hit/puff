from django.contrib import admin
from django.urls import path, include

from puff import urls as puff_urls, views as puff_views
from user import urls as user_urls

admin.site.enable_nav_sidebar = False
admin.site.site_header = ' '

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', puff_views.home, name='home'),
    path('puffs', include(puff_urls.urlpatterns)),
    path('user', include(user_urls.urlpatterns)),
]
