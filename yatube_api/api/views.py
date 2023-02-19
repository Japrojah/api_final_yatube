from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import AuthorOrReadOnly
from posts.models import Post, Group


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет работает с PostSerializer.
    Наследован от ModelViewset,
    Добавлена пагинация,
    Переопределён метод perform_create."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет работает с CommentSerializer.
    Наследован от ModelViewset,
    Переопределён метод get_queryset & perform_create."""

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_post(self, post_id):
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        return self.get_post(self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post(self.kwargs.get('post_id'))
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет работает с GroupSerializer.
    Наследован от ModelViewset."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    """Вьюсет работает с FollowSerializer.
    Наследован от mixins таких как:
    CreateModelMixin, GenericViewSet, ListModelMixin,
    Добавлена возможность фильтрации,
    Переопределён метод get_queryset & perform_create."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
