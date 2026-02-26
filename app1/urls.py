from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



    
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [

    path('home/',views.home,name="home"),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name="."),
    path('abc/',views.abc,name="abc"),
    path('signup/',views.signup_view,name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout' ),
    path('update/', views.update_profile, name='update_profile'),
    path('api/', include(router.urls)),    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]