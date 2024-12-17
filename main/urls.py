from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.urls import include



urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.submit_contact, name='submit_contact'),
    path('wikipedia_page/', views.wikipedia_page, name='wikipedia'),
    path('register/', views.register, name='register'),
    path('support/', views.support, name='support'),
    path('learners/', views.learners_page, name='learners'),
    path('learners/', views.learners_page, name='learners_page'),

  

    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('donate/', views.donate_view, name='donate'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),  # Fixed route
    
    path("mpesa/stk_push/", views.process_donation, name="mpesa_stk_push"),
    
    path('admin/', admin.site.urls),
    path('files/', include('file_manager.urls')),
    

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]




