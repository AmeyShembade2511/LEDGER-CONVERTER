from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name="home"),
    path('download',views.download,name="download"),
    path('convert',views.convert,name="convert"),
    path('waprfile',views.waprfile,name="waprfile")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



