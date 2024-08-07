from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView, UsersListView, RelatedUsersListView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("registration/", UserRegistrationView.as_view(), name="user_registration"),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("related_users/", RelatedUsersListView.as_view(), name="related_users_list"),
]
