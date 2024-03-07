from rest_framework import serializers

from .models import Category, Comment, Rating, Request, RequestStatus, User


class CommentSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    request = serializers.SlugRelatedField(slug_field='name_required', queryset=Request.objects.all())
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = ('text', 'created', 'request', 'user')
        read_only_fields = ('created',)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class RequestSerializer(serializers.ModelSerializer):
    request_category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    status = serializers.SlugRelatedField(slug_field='status_name', queryset=RequestStatus.objects.all())
    ratings = serializers.SlugRelatedField(slug_field='value', queryset=Rating.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Request
        fields = ('id', 'name_required',
                  'description', 'start_date', 'end_date',
                  'request_category', 'status',
                  'ratings', 'user')
