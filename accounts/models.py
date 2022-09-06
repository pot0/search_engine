from distutils.command.upload import upload
from ssl import Options
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.

#서로의 모델 접근 1:1 (하나의 사용자는 하나의 프로필 가짐)
'''
class UserManager(BaseUserManager):
    def create_user(self, name, password=None):
        """
        주어진 네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not name:
            raise ValueError(_('Users must have an name'))

        user = self.model(
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, last_name, first_name, password):
        """
        주어진 네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            password=password,
            name=name,
        )

        user.is_superuser = True #모든 권한이 있음을 지정
        user.save(using=self._db)
        return user
'''

class User(AbstractUser):
    user = models.CharField(verbose_name='이름', max_length=64)
    image = models.ImageField(verbose_name="프로필사진", upload_to ="")
    #objects = UserManager()

    def __str__(self):
        return self.username

