from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    #camkdsnfkdngkdfng

    def create_user(self,  ci, first_name, last_name, password=None, email=None, **extra_fields):
        if not ci or len(ci) != 11:
            raise ValueError('El carnet de identidad debe tener exactamente 11 dígitos')

        user = self.model(ci=ci, first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ci, password=None,  email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(ci=ci, first_name='', last_name='', password=password, **extra_fields)


class CustomUser (AbstractUser):
    ci = models.CharField(max_length=11)
    email = models.EmailField(_("email address"), blank=True, null=True)
    REQUIRED_FIELDS = ["ci", "password"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    objects = CustomUserManager()

    @classmethod
    def create_user(self, ci, first_name, last_name, password=None, email=None, **extra_fields):
        if not ci or len(ci) != 11:
            raise ValueError('El carnet de identidad debe tener exactamente 11 dígitos')

        user = self.model(ci=ci, first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # ==== Cambio de contraseña:
    def set_new_password(self, new_password):
        self.set_password(new_password)
        self.save()

    def clean(self):
        super().clean()
        if CustomUser.objects.exclude(pk=self.pk).filter(email=self.email).exists()  and self.email :
            raise ValidationError('El email debe ser único')