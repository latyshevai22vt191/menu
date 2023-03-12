from django.urls import path

from .views import *

urlpatterns = [
    path('menu', get_parent_category),
    path('menu/<int:id>/', get_category, name='get_id')
]
