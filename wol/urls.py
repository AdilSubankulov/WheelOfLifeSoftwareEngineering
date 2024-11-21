from django.urls import path, re_path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]