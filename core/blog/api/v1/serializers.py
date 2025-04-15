from rest_framework import serializers

from ...models import Post, Category




# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url')
    class Meta:
        model = Post
        fields = ["id", "status", "image", "title", "content", "snippet", "category", "relative_url", "created_date", "updated_date"]


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]

    