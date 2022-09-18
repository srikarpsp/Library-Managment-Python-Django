from django.urls import path, include
from rest_framework import routers
from Employee_Registration import views
from rest_framework import viewsets 
#from .views import EmployeePostRudView, EmployeePostAPIView

router = routers.DefaultRouter()
router.register('Employee_Registration', views.EmployeeView)

#routeList = (
 #   ('postings', PostingsViewSet),
#)
urlpatterns = [
    path('v1/',include(router.urls))
]   
