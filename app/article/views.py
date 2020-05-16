
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from core.models import Article, Author
from .serializers import ArticleSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(
            Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def list(self, request, *args, **kwargs):
        response = self.get_queryset()
        serializer = self.get_serializer(response, many=True)
        data = {
            'message': 'successfuly have data',
            'articles': serializer.data,
        }
        return Response(data)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
