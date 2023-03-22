from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:post-detail-api', read_only=True
    )
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'author',
            'title',
            'author',
            'body',
            'created',
            'updated',
        ]
