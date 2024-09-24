from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserRegisterAPIView, UserGet, UpdateUserAPIView, GetAllUsersAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('profile/', UserGet.as_view(), name='profile'),
    path('update/', UpdateUserAPIView.as_view(), name='update_user'),
    path('get_users', GetAllUsersAPIView.as_view(), name='get_users')

]