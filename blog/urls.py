from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.get_post, name='get_post'),
    path('comment/<int:post_id>/new', views.post_comment, name='post_comment'),
    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]