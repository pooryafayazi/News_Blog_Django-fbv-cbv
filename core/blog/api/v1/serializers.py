from rest_framework import serializers

from ...models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url')
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["id", "status", "image", "title", "content", "snippet", "category", "relative_url", "absolute_url", "created_date", "updated_date"]

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep


    