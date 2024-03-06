from rest_framework import viewsets
from electro_zaiavka.serializers import RequestSerializer, CommentSerializer
from .models import Request, Comment, User


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class RequestApiView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

