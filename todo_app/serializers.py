from rest_framework import serializers

from.models import ToDo


class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    is_completed =serializers.BooleanField(required=False)
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()


class UpdateToDoSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    deadline = serializers.DateTimeField(required=False)
    is_completed = serializers.BooleanField(required=False)

    def update(self, instance: ToDo, validated_data: dict) -> ToDo: 
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # instance.title = validated_data.get('title', instance.title)
        # instance.deadline = validated_data.get('deadline', instance.deadline)
        # instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance