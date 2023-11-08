from django.urls import path
from . import views
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('todo',views.TodoViewSet,basename='todo')

urlpatterns = [
    
    
]

urlpatterns += routers.urls