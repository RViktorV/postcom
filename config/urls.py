from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # URL для административной панели Django
    path("users/", include("users.urls")),  # Включаем маршруты из приложения users
    path(
        "content/", include("content.urls")
    ),  # Включаем маршруты из приложения content
]
