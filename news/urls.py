from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)


urlpatterns = [
    path('comment/', views.CommentListCreateView.as_view(), name='comment_list'),
    path('comment/<int:id>/', views.CommentUpdateDelete.as_view(), name='comment_up_del'),
    path('', include(router.urls)),
]