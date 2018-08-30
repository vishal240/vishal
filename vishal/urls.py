from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path('', include('posts.urls')),
    path('mark/', include('mark.urls')),
    path('admin/', admin.site.urls),
]
