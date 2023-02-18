from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, User, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    """Cериализатор для модели Post.
    Работает со всеми полями модели,
    Переопределено поле author."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализоватор для модели Comments.
    Работает со всеми полями модели,
    Переопределены полня author и post."""

    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = SlugRelatedField(
        read_only=True,
        slug_field='pk'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализоватор для модели Group.
    Работает со всеми полями модели."""

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализоватор для модели Follow.
    Работает со всеми полями модели,
    Переопределены поля user & following,
    Настроен метод валидации."""
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following',)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Подписка уже существует'
            )
        ]

    def validate(self, data):
        user = self.context['request'].user
        follow = data['following']
        if user == follow:
            raise serializers.ValidationError(
                "Невозможно подписаться на себя"
            )
        return data
