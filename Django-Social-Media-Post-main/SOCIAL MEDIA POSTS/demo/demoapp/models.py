from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='post/',null=True,blank=True)
    desc=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True,null=True)
    liked=models.ManyToManyField(User)
    hide=models.BooleanField(default=False)

    def like_count(self):
        return self.liked.count()

class product_comments(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='cmt')
    name_cmt=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cmt_user')
    body=models.TextField()
    date_cmt=models.DateTimeField(auto_now_add=True,null=True)
