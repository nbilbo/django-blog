from django.views.generic import DetailView, ListView
from django.utils.text import slugify

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        data = serializer.validated_data
        slug = slugify(data.get('title'))
        author = self.request.user
        serializer.save(author=author, slug=slug)


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        data = serializer.validated_data
        slug = slugify(data.get('title'))
        serializer.save(slug=slug)


@api_view(['GET'])
def api_view(request, format=None):
    return Response(
        {
            'posts': reverse(
                'blog:post-list-api', request=request, format=format
            )
        }
    )
