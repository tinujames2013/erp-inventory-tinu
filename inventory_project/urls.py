from django.contrib import admin
from django.urls import path, include, re_path
from inventory_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory_app.urls')),
    re_path(r'^.*$', index),  # Catch-all for Vue frontend
]
