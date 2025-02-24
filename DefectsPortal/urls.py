from django.urls import path
from DefectsPortal import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('', views.defect, name='defect'),
    path('descr/<int:id>/', views.defect_description, name='descr'),
    path('add/', views.add_defect, name='add'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)