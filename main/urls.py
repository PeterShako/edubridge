from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('attempts/', views.attempts, name='attempts'),
    path('assessment/', views.assessment, name='assessment'),
    path('home/', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.submit_contact, name='submit_contact'),
    path('wikipedia_page/', views.wikipedia_page, name='wikipedia'),
    path('register/', views.register, name='register'),
    path('libraries/', views.libraries, name='libraries'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    
    #lessons
    path('lesson1/', views.lesson1, name='lesson1'),
    path('lesson2/', views.lesson2, name='lesson2'),
    path('lesson3/', views.lesson3, name='lesson3'),
    path('lesson4/', views.lesson4, name='lesson4'),
    path('lesson5/', views.lesson5, name='lesson5'),
    path('lesson6/', views.lesson6, name='lesson6'),
    path('lesson7/', views.lesson7, name='lesson7'),
    path('lesson8/', views.lesson8, name='lesson8'),
    path('lesson9/', views.lesson9, name='lesson9'),
    path('lesson10/', views.lesson10, name='lesson10'),
    path('lesson11/', views.lesson11, name='lesson11'),
    path('lesson12/', views.lesson12, name='lesson12'),
    path('lesson13/', views.lesson13, name='lesson13'),
    path('lesson14/', views.lesson14, name='lesson14'),
    path('lesson15/', views.lesson15, name='lesson15'),
    
    
    path('progress/', views.progress, name='progress'),
    path('dev/', views.dev, name='dev'),
    path('learners/', views.learners_page, name='learners'),
    path('learners/', views.learners_page, name='learners_page'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/', views.view_notes, name='view_notes'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('notes/<int:id>/', views.note_detail, name='note_detail'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('donate/', views.donate_view, name='donate'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),  
    path("mpesa/stk_push/", views.process_donation, name="mpesa_stk_push"),
    path('admin/', admin.site.urls),
    path('files/', include('file_manager.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('notes/', views.view_notes, name='view_notes'),  # View all notes
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),  # View full note
]




