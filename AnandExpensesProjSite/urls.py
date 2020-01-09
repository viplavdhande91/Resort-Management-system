"""AnandExpensesProjSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
import Employee_App.views, Employee_App.urls, Employee_App.views_advance, Employee_App.views_attendance, Employee_App.views_salary
from django.conf import settings
import Personal_App.views, Personal_App.urls
from django.conf.urls.static import static # new
admin.autodiscover()


urlpatterns = [
         #\path('admin_tools/', include('admin_tools.urls')),
         #path('attendance_Of_Any_month/', include('Employee_App.urls')),

         path('tables/', admin.site.urls),

        # path('mysite/', include('Employee_App.urls')),
         path('', include('Employee_App.urls')),

         path('todo/', include('Personal_App.urls')),



         
       ]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	

admin.site.site_header = "Neha Admin"
admin.site.site_title = "Neha Personal Portal"
admin.site.index_title = "Neha's Site"