from django.contrib import admin
from django.urls import path
from meninoDjango.views import home, dashboard, landingpage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('landing/', landingpage, name='landingpage'),
]