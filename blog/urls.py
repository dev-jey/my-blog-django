
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (handler404, handler500)

handler404 = 'app.views.error404'
handler500 = 'app.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
