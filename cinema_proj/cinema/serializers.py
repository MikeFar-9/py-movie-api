from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   title = serializers.CharField(required=True, max_length=255)
   description = serializers.TextField(required=False)
   duration = serializers.IntegerField(required=True)

   def create(self, validated_data):
       return Movie.objects.create(**validated_data)

   def update(self, instance, validated_data):
       instance.info = validated_data.get("info", instance.info)
       instance.duration = validated_data.get(
           "duration",
           instance.duration
       )
       instance.save()
       return instance
