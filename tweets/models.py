from django.db import models

"""

새로운 Django 프로젝트를 생성하고, 이를 깃허브에 업로드 하세요.
tweets 라는 이름의 앱을 생성하고 설치하세요.
tweets앱은 Tweet 그리고 Like 라는 models 이 있어야 합니다.
Tweet 그리고 Like models 을 위한 어드민을 만드세요.
Tweet Model Fields
payload: Text(max. lenght 180)
user: ForeignKey
created_at: Date
updated_at: Date
Like
user: ForeignKey
tweet: ForeignKey
created_at: Date
updated_at: Date
Requirements:
abstract 클래스를 사용하세요.
모든 클래스의 __str__ 메소드를 커스터마이즈 하세요.

"""


class AbstactTimeStampedModel(models.Model):
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        abstract = True


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tweet(AbstactTimeStampedModel):
    payload = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.payload


class Like(AbstactTimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.tweet}"
