
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_post),
    path('<int:pk>/',views.get_post),
    path('delete/<int:pk>/',views.delete_post),
    path('comments/<int:post_id>',views.get_comment)
]