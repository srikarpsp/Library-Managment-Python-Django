from django.urls import path, include
from rest_framework import routers
from . import views 
#from .views import EmployeePostRudView, EmployeePostAPIView

router = routers.DefaultRouter()
router.register('assignbook', views.AssignbookView)
router.register('bookdetails', views.BookdetailsView)

#routeList = (
    #('assignbook', AssignBookViewSet),
   # ('employeename', EmployeenameViewSet),
  #  ('bookname', BooknameViewSet),
 #   ('employee', EmployeeViewSet),
#)
urlpatterns = [
    path('v1/',include(router.urls))
]   
