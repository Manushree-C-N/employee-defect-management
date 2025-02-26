from django.urls import path
from DefectsPortal import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.defect, name='defect'),
    path('descr/<int:id>/', views.defect_description, name='descr'),
    path('add/', views.add_defect, name='add'),
    path('edit/<int:id>/', views.update_defects, name='edit'),  # Updated URL pattern
    path('deletes/<int:id>/', views.delete_defects, name='deletes'),  # Delete URL pattern

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)