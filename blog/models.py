from django.db import models
from django.contrib.auth.models import User

import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    # blank=True는 필수 입력값이 아니라는 뜻
    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)

    # auto_now_add=True 를 해줘야 추후에 글 생성시, 시간 등을 선택하지 않고 자동반영 될 수 있음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CASCADE는 해당 작성자가 데이터베이스에서 삭제되면, 그 작성자가 작성한 포스트도 함께 삭제한다.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # SET_NULL은 해당 작성자가 데이터베이스에서 삭제되면, 그 작성자가 작성한 포스트 작성자 명은 공란이 된다.
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # f-string 기법
    def __str__(self):
        # 포스트의 pk 값 , 포스트의 title 값
        return f"[{self.pk}] {self.title} :: {self.author}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split(',')[-1]