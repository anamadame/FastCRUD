from django.urls import path, include, re_path
from .views import *


urlpatterns = [

    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),

    path('user_profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('user_profiles/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),

    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),


    path('foods/', FoodViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='food_list'),
    path('foods/<int:pk>/', FoodViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='food_detail'),




    path('ratings/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='ratings_list'),
    path('ratings/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='ratings_detail'),


    path('food_photos/', FoodPhotoViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='food_photos_list'),
    path('food_photos/<int:pk>/', FoodPhotoViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='food_photos_detail'),


    path('comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='comments_list'),
    path('comments/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comments_detail'),

]