from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class SoftDeleteModel(models.Model):
    class Meta:
        abstract = True
        
    created_at = models.DateTimeField(auto_now_add=True ,blank=False, null=False, help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, help_text="Fecha de actualización")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="Fecha de eliminación")
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def recover(self):
        self.deleted_at = None
        self.save()

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser establecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, SoftDeleteModel):
    email = models.EmailField(unique=True, null=False, blank=False)
    password_hash = models.CharField(blank=False, max_length=2000, null=False)
    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Se pueden agregar otros campos requeridos aquí

    class Meta:
        default_permissions = ()
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def set_password(self, password):
        # Aquí deberías utilizar un algoritmo más seguro que MD5, como bcrypt
        pass

    def check_password(self, password):
        # Método para comparar la contraseña guardada con la ingresada
        pass