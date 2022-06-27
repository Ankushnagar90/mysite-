from django.urls import path
# from api_view.api_views import PostListAPIView,PostDetailAPIView,UserLoginAPI,UserLogoutAPI,UpdateProfileView,DeleteAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns
from api_view import api_views
from api_view.api_views import PostViewSet, UserViewSet, api_root
from rest_framework import renderers


schema_view = get_schema_view(
   openapi.Info(
      title="Mysite Project API",
      default_version='v1',
      description="User description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


def trigger_error(request):
    division_by_zero = 1 / 0

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',	
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'   
})


urlpatterns = format_suffix_patterns([
	path('', api_root),
    path('snippets/', post_list, name='snippet-list'),
    path('snippets/<int:pk>/', post_detail, name='post-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('sentry-debug/', trigger_error),
])	
	# path('', PostListAPIView.as_view()),
	# path('login/', UserLoginAPI.as_view(), name='login'),
	# path('logout/', UserLogoutAPI.as_view(), name='logout'),
	# path('update/<int:pk>', UpdateProfileView.as_view(), name='update'),
	# path('delete/', DeleteAPIView.as_view(), name='delete'),
	# path('detail/<int:pk>', PostDetailAPIView.as_view()),