from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import FoodFilter


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()  # добавляем вызов .all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # добавляем вызов .all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class FoodViewSets(viewsets.ModelViewSet):
    queryset = Food.objects.all()  # добавляем вызов .all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FoodFilter
    search_fields = ['title']





class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()  # добавляем вызов .all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['stars']


class FoodPhotoViewSets(viewsets.ModelViewSet):
    queryset = FoodPhoto.objects.all()  # добавляем вызов .all()
    serializer_class = FoodPhotoSerializer
    permission_classes = [permissions.AllowAny]


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # добавляем вызов .all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


