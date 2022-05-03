# import ModelSerializer for serializer models
from rest_framework.serializers import ModelSerializer
from post.models import Post
from django.contrib.auth.models import User

# specify serializer of post model (for all fields)
class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# specify serializer of User model (for all fields)
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'