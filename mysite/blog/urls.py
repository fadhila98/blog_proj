from django.urls import path, include
from .views import (
    BlogDeleteView,
    BlogUpdateView,
    BlogCreateView,
    BlogDetailView,
    BlogListView,
    BlogModel
)


app_name = 'blog'
urlpatterns = [
    # path('', views.index, name= 'index'),
    path('',BlogListView.as_view(), name= 'blog-list'),
    path('<int:id>/',BlogDetailView.as_view(), name = 'blogmodel-detail'),
    path('create/',BlogCreateView.as_view(), name = 'blog-create'),
    path('<int:id>/update/',BlogUpdateView.as_view(), name = 'blog-update'),
    path('<int:id>/delete/',BlogDeleteView.as_view(), name = 'blog-delete'),



]