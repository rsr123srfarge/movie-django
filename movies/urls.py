
from django.contrib import admin
from django.urls import path
from movies import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',views.movies),
    path('HomePage/',views.HomePage),
    path('index/',views.index)
      
]
