from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer, UsersListSerializer
from .models import CustomUser

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UsersListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated,)