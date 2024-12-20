from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.submit_contact, name='submit_contact'),
    path('wikipedia_page/', views.wikipedia_page, name='wikipedia'),
    path('register/', views.register, name='register'),
    
    path('learners/', views.learners_page, name='learners'),
    path('learners/', views.learners_page, name='learners_page'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/', views.view_notes, name='view_notes'),  # URL for viewing notes
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('notes/<int:id>/', views.note_detail, name='note_detail'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('donate/', views.donate_view, name='donate'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),  # Fixed route
    
    path("mpesa/stk_push/", views.process_donation, name="mpesa_stk_push"),
    path('learners/', views.learners_page, name='learners_page'),
    path('admin/', admin.site.urls),
    path('files/', include('file_manager.urls')),
    

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('notes/', views.view_notes, name='view_notes'),  # View all notes
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),  # View full note


]




