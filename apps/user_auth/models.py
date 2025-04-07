from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class BaseModel(models.Model):
    """
    Abstract base model that provides common fields and methods.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(_('email address'), unique=True, max_length=255)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150, null=True, blank=True)
    country_code = models.CharField(_('country code'), max_length=4)
    mobile = models.CharField(_('mobile number'), max_length=15)
    address = models.TextField(_('address'))
    country = models.CharField(_('country'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    pin_code = models.CharField(_('pin code'), max_length=10)
    fax = models.CharField(_('fax'), max_length=15, null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=15, null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'
        unique_together = ('email', 'mobile')
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def get_full_address(self):
        return f"{self.address}, {self.city}, {self.pin_code}, {self.country}"