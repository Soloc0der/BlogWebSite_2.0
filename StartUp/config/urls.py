from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('posts.urls')), 
    path('blog/', include('blog.urls')),
    # path('admin-star/', include('admin_star.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)