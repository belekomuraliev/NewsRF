from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response


from .serializers import CommentSerializer, PostSerializer
from .models import Post, Comment


class PostViewSet(ViewSet, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentUpdateDelete(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        serializer= self.serializer_class(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

