from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, enroll_id, password=None):
        if not username:
            raise ValueError("Users must have an Username")
        # if not enroll_id:
            # raise ValueError("Users must have an Enroll Identification Number")
        
        user = self.model(
            username=username,
            enroll_id=enroll_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username, is_student, password, enroll_id):
        user = self.create_user(
            username=username,
            enroll_id=enroll_id,
            password=password,
        )
        user.is_student = False
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    enroll_id = models.IntegerField(unique=True, null=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'enroll_id'
    REQUIRED_FIELDS = ['username', 'is_student']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
