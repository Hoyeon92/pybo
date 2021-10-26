from django.db import models
from django.contrib.auth.models import User


# 모델을 변경한 후에는 반드시 makemigrations와 migrate를 통해 DB를 변경해야 함
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # author 필드는 User 모델을 ForeignKey로 적용하여 선언
    subject = models.CharField(max_length=200)        # on_delete=models.CASCADE : 계정이 삭제되면 계정이 작성한 질문을 모두 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   # DB에서 수정일시 컬럼에 null허용, blank=True : form.is_valid()를 통한 입력데이터 검사 시, 값이 없어도 된다는 의미
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')   # author : 글쓴이
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   # 어떤 조건으로든 값을 비워둘 수 있음을 의미, 수정일시는 수정한 경우에만 생성되는 데이터이므로 null=True, blank=True를 지정
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)   # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)       # 이 댓글이 달린 답변
