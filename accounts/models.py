from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
        def create_user(self,email,name,college_name,password=None):
            if not email:
                raise ValueError("Users must have an email")
            if not name:
                raise ValueError("Users must have a name")


            user = self.model(email=self.normalize_email(email),
                              name=name,college_name=college_name)
            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_superuser(self,email,name,password):
            user = self.create_user(email=self.normalize_email(email),name=name,password=password)

            user.is_admin=True
            user.is_staff=True
            user.is_superuser=True
            user.save(using=self._db)

            return user

class users(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=100,unique=True)
    name = models.CharField(max_length=50,unique=True)
    college_name = models.TextField()
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login",auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','college_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True

