from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from electro_zaiavka.models import Comment, Request
from electro_zaiavka.serializers import CommentSerializer, RequestSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.filter(user=user)
        return queryset




class RequestApiView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Request.objects.filter(user=user)
        return queryset
