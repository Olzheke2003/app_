from rest_framework import viewsets
from electro_zaiavka.serializers import RequestSerializer, CommentSerializer
from .models import Request, Comment, User


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        request_id = self.request.get('request_pk')
        queryset = Comment.objects.filter(request=request_id)
        return queryset


class RequestApiView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

