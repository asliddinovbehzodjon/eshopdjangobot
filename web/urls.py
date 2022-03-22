from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header='Behzod Eshop Bot Adminstration'
urlpatterns = [
    path('owner/', admin.site.urls),
    path('api/v1/',include('app.urls'))
]
