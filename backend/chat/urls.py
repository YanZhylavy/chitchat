from django.urls import path
from .views import CreateConversationView, RetrieveConversationView

urlpatterns = [
    path("create/", CreateConversationView.as_view(), name="create_conversation"),
    path("conversation/", RetrieveConversationView.as_view(), name="retrieve_conversation"),
]