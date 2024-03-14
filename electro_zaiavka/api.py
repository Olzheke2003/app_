from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from electro_zaiavka.models import Comment, Request, User
from electro_zaiavka.serializers import CommentSerializer, RequestSerializer, UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)


class RequestApiView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and not user.work:
            queryset = Request.objects.filter(request_category=user.category)
        else:
            queryset = Request.objects.all()
        return queryset


class UserUpdateApiView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user
