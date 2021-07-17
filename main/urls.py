from django.urls import path
from .views import PlaceDelete, PlaceList, PlaceDetail, PlaceCreate, PlaceUpdate, UserLogin, UserRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', PlaceList.as_view(), name='places'),
    path('details/<int:pk>/', PlaceDetail.as_view(), name='details'),
    path('create/', PlaceCreate.as_view(), name='form'),
    path('update/<int:pk>/', PlaceUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PlaceDelete.as_view(), name='delete'),
]
