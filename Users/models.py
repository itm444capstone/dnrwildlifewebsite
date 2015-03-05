from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.
class AccountManager(BaseUserManager):
    """
        The account manager model. Handles the creation of
        accounts.
    """
    def _create_user(self, username, password, first_name, last_name,
                     email, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Username must be filled in')
        if not password:
            raise ValueError('Password must be filled in')
        if not first_name:
            raise ValueError('First Name must be filled in')
        if not last_name:
            raise ValueError('Last Name must be filled in')
        if not email:
            raise ValueError("Email must be filled in")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                first_name=first_name, last_name=last_name,
                is_active=True, is_staff=is_staff,
                is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, first_name, last_name, email,
            password=None, **extra_fields):
        return self._create_user(username, password, first_name, last_name,
                False, False, **extra_fields)

    def create_superuser(self, username, first_name, last_name, email,
            password, **extra_fields):
        return self._create_user(username, password, first_name, last_name,
                email, True, True, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    """
        This is the user account model. All users in the system will
        be represented by this model.
    """

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=70, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField('Staff Status', default=False)
    is_active = models.BooleanField('Active', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = AccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return "%s" % self.first_name

