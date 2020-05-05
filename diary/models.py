from django.db import models
from django.contrib.auth import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # 현재의 시간 값을 디폴트값으로 받아가는 date
    date = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)