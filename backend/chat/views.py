from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateConversationSerializer
from .managers import MongoManager as mngr


class CreateConversationView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request):
        serializer = CreateConversationSerializer(
            data=request.data, context={"request": request})    
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RetrieveConversationView(APIView):
    permission_classes = (IsAuthenticated,)    

    def get(self, request: Request):
        user_id = request.user.id
        companion_id = int(request.query_params.get("companion"))
        chunk = int(request.query_params.get("chunk"))
        conv_id = mngr.get_conversation(user_id, companion_id)
        data = mngr.get_paginated_messages(conv_id, chunk)
        return Response(data, status=status.HTTP_200_OK)
