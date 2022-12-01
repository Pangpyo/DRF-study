from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        # 주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        if not email:
            raise ValueError("유저 이메일이 없습니다.")
        if not username:
            raise ValueError("유저 네임이 없습니다.")

        user = self.model(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        # """
        # 주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        # 단, 최상위 사용자이므로 권한을 부여
        # """
        superuser = self.create_user(
            email=email,
            password=password,
            username=username,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=30, unique=True, null=True, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    # 유저네임필드는 빠지면 안됨 ( 이메일로 안써도 됨, 대신에 유니크 값을 넣어줘야함,)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
