from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"table", views.BookingViewSet)

urlpatterns = [
    path("booking/", include(router.urls)),
    path("menu-items", views.MenuItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("api-token-url", obtain_auth_token)
]