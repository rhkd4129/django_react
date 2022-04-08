
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer,CommentSerializer
from .models import Post,Comment
from rest_framework.permissions import AllowAny

from instagram import models

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [AllowAny] # FIXME :인증적용

    #    def perform_create(self, serializer):
    #     # post = form.save(commit=False)
    #     # post.author = self.request.user
    #     # post.save()
    #     serializer.save(author=self.request.user)
    #     return super().perform_create(serializer)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__pk = self.kwargs["post_pk"])
        return qs
        
 