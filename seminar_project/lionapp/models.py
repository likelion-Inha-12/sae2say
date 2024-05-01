from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=200)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="commenter")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

class UserPost(models.Model):
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="posts")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="users")