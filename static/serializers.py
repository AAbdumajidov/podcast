from django.contrib.auth.models import User
from rest_framework import serializers

from singer.models import Singer
from ..models import Category, Tag, Season, Episode, Comment, Like, Playlist, PlayListItem, Music


class CategoriSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = ['id', 'user', 'image']


class ArticleSerializer(serializers.ModelSerializer):
    category = CategoriSerializer(read_only=True)
    tag = TagsSerializer(read_only=True, many=True)
    singer = MiniSerializer(read_only=True)

    class Meta:
        model = Episode
        fields = ['id', 'singer', 'title', 'description', 'season', 'image', 'song', 'created_date', 'category', 'tag']


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ['id', 'singer', 'title', 'description', 'season', 'image', 'song', 'created_date', 'category', 'tag']

    def create(self, validated_data):
        request = self.context.get('request')
        singer = request.user.singer
        instance = super().create(validated_data)
        instance.singer = singer
        instance.save()
        return instance


class CommetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date', 'name', 'is_anonymous', 'image']
        extra_kwargs = {
            'blog': {'required': False}
        }

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.singer.id
        description = validated_data.get('description')
        name = validated_data.get('name')
        instance = Comment.objects.create(ar=blog_id, author_id=author_id, description=description, name=name)
        return instance


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'title']
        extra_kwargs = {
            'title': {'required': False}
        }


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['author', 'music']


class MiniMusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MiniPlayListItemSerializers(serializers.ModelSerializer):
    music = MiniMusicSerializers(read_only=True)

    class Meta:
        model = PlayListItem
        fields = ['id', 'music']


class PlaylistSerializers(serializers.ModelSerializer):
    items = MiniPlayListItemSerializers(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'items']


class PlaylistGetSerializers(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'items']