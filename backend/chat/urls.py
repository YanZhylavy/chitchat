from django.urls import path
from .views import CreateConversationView

urlpatterns = [
    path("create/", CreateConversationView.as_view(), name="create_conversation"),
]