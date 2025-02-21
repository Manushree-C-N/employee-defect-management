from django.urls import path
from DefectsPortal import views


urlpatterns = [
    path('', views.defect, name='defect'),
    path('descr/<int:id>/', views.defect_description, name='descr'),
]