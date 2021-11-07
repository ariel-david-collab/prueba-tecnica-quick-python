# Author: Ariel David Herrera Ahumada
# Date: 2021-11-06
# Version: 1.0.0

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, date_birth, mobile_phone, email, password, address):
        # custom user model
        if not mobile_phone:
            raise ValueError("Users must have an mobile phone")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            mobile_phone=mobile_phone,
            email=self.normalize_email(email),
            address=address,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, date_birth, mobile_phone, email, password, address):
        # custom superuser model
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            mobile_phone=mobile_phone,
            email=email,
            password=password,
            address=address,
        )

        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # custom user model
    document_type_id = models.CharField(max_length=2, null=True, blank=True)
    document_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    session_active = models.BooleanField(default=False)
    date_birth = models.DateField(auto_now=False, null=False, auto_now_add=False)
    email = models.EmailField(max_length=254, null=False)
    mobile_phone = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=120, null=False)
    address = models.CharField(max_length=50, null=False)
    token = models.CharField(max_length=120, null=True, blank=True)
    city_id = models.CharField(max_length=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserAccountManager()

    # set the mobile_phone as username
    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "date_birth", "password", "address"]

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.first_name
