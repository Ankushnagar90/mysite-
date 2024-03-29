"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api_view import api_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'PostAPI', api_views.PostViewSet,basename="post")
router.register(r'userAPI', api_views.UserViewSet,basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('api/', include('api_url.api_urls')),    
    path('api-auth/', include('rest_framework.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('', include('myapp.urls')),
    # path('accounts/', include('social_django.urls', namespace='social'))

    # path('accounts/', include('allauth.urls')),
    # path('sentry-debug/', trigger_error),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




