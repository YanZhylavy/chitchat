from rest_framework import serializers
from .managers import MongoManager as mngr
from authentication.models import CustomUser


class CreateConversationSerializer(serializers.Serializer):
    participant_id = serializers.IntegerField()

    def create(self, validated_data):
        request = self.context.get("request")
        initiator_id = request.user.pk
        participant_id = validated_data.get("participant_id")
        request.user.related_users.add(
            CustomUser.objects.get(pk=participant_id))
        return mngr.create_conversation(initiator_id, participant_id)
