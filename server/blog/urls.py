from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls')),
    path('', include('home.urls')),
    path('', include('comments.urls')),
    path('', include('posts.urls')),
    path('', include('userprofiles.urls'))
]
