from django.urls import path
from .views import *

urlpatterns = [
    path('', files.as_view(), name='files-list'),
    path('<int:pk>', file.as_view(), name='file-detail'),    
]
