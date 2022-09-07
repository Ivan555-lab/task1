from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('shop84.urls', namespace='blog')),
]

#from django.urls import path, include
#from django.contrib import admin