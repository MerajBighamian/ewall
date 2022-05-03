from django.shortcuts import render
# import all generic views
from rest_framework.generics import * 
from post.models import Post
# import serializers
from .serializers import PostsSerializer, UserSerializer
# import permissions of drf
from rest_framework.permissions import IsAuthenticated
# import customize permissions
from .permissions import IsAuthorOrReadOnly
# Create your views here.

# view for show list of posts
class PostsList(ListAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostsSerializer

# view for Delete Post (with id of post)
class DeletePost(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly)

# view for Create post 
class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)


# view for retrieve and update a post with id   
class UpdatePost(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly)

# view for retrieve Post with id
class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

# view for show list of post (post of special user (currently user is authenticated))
class MyPostsList(ListAPIView):
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly)

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    