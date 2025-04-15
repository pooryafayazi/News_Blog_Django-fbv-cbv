from rest_framework import serializers

from ...models import Post




# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ["id", "status", "image", "title", "content", "created_date", "updated_date"]




