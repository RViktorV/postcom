from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateView, UserListView, UserDetailView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),  # GET /users/
    path(
        "create/", UserCreateView.as_view(), name="user-create"
    ),  # POST /users/create/
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),  # GET /users/<id>/
    path("login/", TokenObtainPairView.as_view(), name="login"),
]
