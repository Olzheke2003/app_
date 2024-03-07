from rest_framework import serializers

from .models import Request, RequestStatus, Category, User, Comment, AbstractUser


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'created', 'request')
        read_only_fields = ('created',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class RequestSerializer(serializers.ModelSerializer):
    request_category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    status = serializers.SlugRelatedField(slug_field='status_name', queryset=RequestStatus.objects.all())
    ratings = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Request
        fields = ('id', 'name_required',
                  'description', 'start_date', 'end_date',
                  'request_category', 'status',
                  'ratings', 'user')

    def get_ratings(self, obj):
        return [rating.value for rating in obj.ratings.all()]

