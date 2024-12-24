from .serializers import (
  UserSerializer, UserRegistrationSerializer, ReviewSerializer,
  CommentSerializer, LikeSerializer, User
)
from movies.models import (
  Movie, Review, Comment, Like
)

from rest_framework import generics


class UserslistAPIView(generics.ListAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

  