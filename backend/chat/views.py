from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateConversationSerializer


class CreateConversationView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = CreateConversationSerializer(
            data=request.data, context={"request": request})    
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
