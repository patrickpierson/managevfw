from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updatedb', views.update_db, name='update_db'),
    path('deletemembers', views.delete_all_members, name='delete_all_members'),
    path('updatememberinfo', views.update_member_info, name='update_member_info')
]
