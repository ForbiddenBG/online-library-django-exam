from django.urls import path

from WebExam3.Profile.views import home_page, profile_page, profile_edit, profile_delete

urlpatterns = (
    path('', home_page, name='index'),
    path('profile/', profile_page, name='profile'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('profile/delete/', profile_delete, name='profile-delete'),
)