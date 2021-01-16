from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime


class AccountManager(BaseUserManager):
    def create_user(self, name, email, county, id_no, phone_number, password=None):
        if not name:
            raise ValueError('name required')
        if not email:
            raise ValueError('email required')
        if not county:
            raise ValueError('county required')
        if not id_no:
            raise ValueError('ID Number required')
        if not phone_number:
            raise ValueError('Phone Number required')
        # if all fields are ok
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            county = county,
            id_no = id_no,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

        #create a super user function 
    def create_superuser(self, name, email, county, id_no, phone_number, password):
        user = self.create_user(
            name=name,
            email=email,
            county = county,
            id_no=id_no,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user



# custom user model
class Users(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,unique=True)
    county = models.CharField(max_length=50)
    id_no = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'county', 'id_no', 'phone_number']

    objects = AccountManager()
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, applabel):
        return True
