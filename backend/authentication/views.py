from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .serializers import UserRegistrationSerializer, UsersListSerializer
from .models import CustomUser

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UsersListView(ListAPIView):
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, )
    search_fields = ["username", "email", "first_name", "last_name"]

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.exclude(id=user.id)    


class RelatedUsersListView(ListAPIView):
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return self.request.user.related_users.all()