from rest_framework import viewsets
from electro_zaiavka.serializers import RequestSerializer, CommentSerializer
from .models import Request, Comment, User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Max


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)


class RequestApiView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Request.objects.filter(user=user)
        return queryset
