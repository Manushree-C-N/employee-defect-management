from django.urls import path
from learnapp import views

urlpatterns = [
    path('',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('edit/',views.userEdit,name='edit')
]
