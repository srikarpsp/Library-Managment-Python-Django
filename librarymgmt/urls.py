"""librarymgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#routeLists = [
 #   postingsUrls.routeList,
  #  libUrls.routeList,
   # apiUrls.routeList,
#]

#router = routers.DefaultRouter()
#for routeList in routeLists:
 #   for route in routeList:
  #      router.register(route[0], route[1])



from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('useraccounts/', include('useraccounts.urls')),
    path('useraccounts/', include('django.contrib.auth.urls')),
    path('', include('Employee_Registration.urls')),
    path('Employee_Registration/', include('Employee_Registration.urls')),
    path('library_management/', include('library_management.urls')),
    #path('', TemplateView.as_view(template_name="ang_home.html"), name='home'),
]
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/useraccounts/', permanent=True)),
]



#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
