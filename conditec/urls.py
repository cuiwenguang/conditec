"""conditec URL Configuration

The `urlpatterns` list routes URLs to api. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function api
    1. Add an import:  from my_app import api
    2. Add a URL to urlpatterns:  path('', api.home, name='home')
Class-based api
    1. Add an import:  from other_app.api import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from conditec.system.api import logout
from conditec.system.router import routers as sys_routers
from raw.router import routers as raw_routers

router = routers.DefaultRouter()

for r in sys_routers:
    router.register(*r)

for r in raw_routers:
    router.register(*r)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', get_swagger_view(title='CondiTec API Docs')),
    path('api/auth/', obtain_auth_token, name='auth'),
    path('api/logout/', logout, name='logout'),
    re_path(r'^api/', include(router.urls), name="rest_framework"),
    path('', TemplateView.as_view(template_name='index.html')),
    # re_path('category(/(?P<action>[a-z]\w*))?(/(?P<id>\d+))?', CategoryController.as_view()),
]