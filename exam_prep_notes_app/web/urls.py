from django.urls import path

from exam_prep_notes_app.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),

    path('add/', views.add_note, name='add note'),
    path('edit/<int:pk>/', views.edit_note, name='edit note'),
    path('delete/<int:pk>/', views.delete_note, name='delete note'),
    path('details/<int:pk>/', views.show_note, name='show note'),

    path('profile/', views.show_profile, name='show profile'),
    path('profile/create/', views.create_profile, name='create profile'),
]
