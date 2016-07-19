# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class FakeModel(models.Model):
    something = models.CharField(max_length=256)

    class Meta:
        permissions = (
            ("do_something", "Can do something"),
            ("do_something_else", "Can do something else"),
        )


class CustomUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True, db_index=True)
    USERNAME_FIELD = 'identifier'

    objects = UserManager()
