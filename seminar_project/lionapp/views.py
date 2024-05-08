import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework import status
from util.views import api_response
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공"
    data = {'message': message}
    return Response(data=data, status=status.HTTP_201_CREATED)

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id' : post.pk,
        '제목' : post.title,
        '내용' : post.content,
        '메시지' : '조회 성공'
    }
    return JsonResponse(data, status=200)

class PostApiView(APIView):

    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        data=[]
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(data=data, message = message, status = status.HTTP_200_OK)

def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "messge":f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용합니다.'})

def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all()
        #    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments")
        return HttpResponse(comment_list, status=200)
    
def like(request, post_id, user_id):
    if request.method == 'PUT':
        user=get_object_or_404(Member, pk=user_id)
        post=get_object_or_404(Post, pk=post_id)

        UserPost.objects.create(user_id=user, post_id=post)
        post.like = post.like+1
        post.save()

        return JsonResponse({}, status=204 )
    return JsonResponse({'message' : '좋아요 반영에 실패하였습니다.'}, status=400)

'''
def addUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')

        user = Member(
            name = name,
            email = email
        )
        user.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})


def createComment(request,post_id,user_id):
    if request.method == 'POST':
        data = json.loads(request.body)

        content = data.get('content')
        user = get_object_or_404(Member, pk=user_id)
        post = get_object_or_404(Post, pk=post_id)

        comment = Comment(
            content=content,
            member_id = user,
            post_id=post
        )

        comment.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})
'''

def return_like(request, post_id):
    if request.method == 'GET':
        post=get_object_or_404(Post, pk=post_id)
        like=post.like
        return JsonResponse({'message':f'like count:{like}'}, status=200)

def top_post(request):
    if request.method == 'GET':
        like_dic = {}
        posts = Post.objects.all()
        for post in posts:
            key = post.title
            val = post.like
            like_dic[key] = val
        sorted_keys = sorted(like_dic, key=like_dic.get, reverse=True)
        top_keys = sorted_keys[:3]
        return JsonResponse(top_keys, status=200, safe=False)
