
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (handler404, handler500)
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'app.views.error404'
handler500 = 'app.views.error500'

urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
