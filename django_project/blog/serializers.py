from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['date_posted']
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author'
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'date_posted': {'read_only': True},
            'author': {'read_only': True}
        }
