# posts/models.py
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

# posts/models.py
from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Prevent multiple likes by the same user
# posts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if not Like.objects.filter(post=post, user=request.user).exists():
            Like.objects.create(post=post, user=request.user)
            # Create notification for the post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(post=post, user=request.user)
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
