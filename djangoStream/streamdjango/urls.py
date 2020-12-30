
from django.urls import path
from django.contrib import admin
from .import views

# url patterns for browsing 

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),
    path('',views.dynamic_stream),
    path('stream/',views.indexscreen),
   ]
