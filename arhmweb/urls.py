from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Path to ADD Karta
    path('add_location', views.add_location, name='add_location'),
    path('edit_location', views.edit_location, name='edit_location'),
    # просмотр и удаление
    path('location/<str:node_id>', views.location, name='location'),
    path(
        'delete_location/<str:node_id>',
        views.delete_location,
        name='delete_location'
        ),

]
