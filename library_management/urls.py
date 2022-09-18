from django.urls import path, include
from rest_framework import routers
from . import views 
#from .views import EmployeePostRudView, EmployeePostAPIView

router = routers.DefaultRouter()
router.register('Book', views.BookView)
router.register('BookType', views.BookTypeView)


urlpatterns = [
    path('', include(router.urls))
]   
