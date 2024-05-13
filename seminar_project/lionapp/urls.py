
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.get_post),
    path('delete/<int:pk>/',views.delete_post),
    path('get_comments/<int:post_id>/',views.get_comment),
    path('like_post/<int:post_id>/<int:user_id>/', views.like),
    #path('addUser/',views.addUser),
    #path('comment/<int:post_id>/<int:user_id>/',views.createComment),
    path('return_like/<int:post_id>/',views.return_like),
    path('top_like/',views.top_post),
    path('v2/post/<int:pk>/', views.PostApiView.as_view()),
    path('v2/post', views.create_post_v2)

]