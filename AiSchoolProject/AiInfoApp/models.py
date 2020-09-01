from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AiClass(models.Model):
    class_num = models.IntegerField()
    teacher = models.CharField(max_length=10)
    class_room = models.CharField(max_length=10)

class AiStudent(models.Model):
    # related_name 은 AiClass의 연결된 AiStudent를 뭘로 부를지 명시
    # on_delete=models.CASCADE는 class 삭제될 때 해당 반의 student도 삭제된다

    participate_class = models.ForeignKey(
        AiClass, on_delete=models.CASCADE, related_name='student'
    )
    # user와 1대1 매칭
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student'
    )
    name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=10)

class StudentPost(models.Model):
    intro = models.TextField()
    # 삭제될 때 null값을 넣자
    # null=True를 꼭 해줘야 한다
    writer = models.ForeignKey(
        AiStudent, related_name='post', on_delete=models.SET_NULL, null=True
    )