# from rest_framework_jwt.views import obtain_jwt_token

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('instagram.urls')),
    # path('token/', obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns +=[
        path("__debug__/",include(debug_toolbar.urls)),
    ]
#...

