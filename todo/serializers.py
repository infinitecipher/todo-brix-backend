from rest_framework import serializers
from todo.models import TodoEntry


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoEntry
        fields = ("__all__")

# class TodoBulkUpdateSerializer(serializers.Serializer)