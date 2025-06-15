from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('api/', include('core.api_urls')),
    path('api/token/', obtain_auth_token),
]
