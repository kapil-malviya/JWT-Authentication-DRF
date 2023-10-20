# Custom User Model and Manager for Email-based Authentication


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

 
# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),          # Normalize email address to lowercase
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True           # Set the superuser as an admin
        user.save(using=self._db)      # Save the superuser to the database
        return user



# Custom user model 
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,             # Ensure that email addresses are unique
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)           # Indicates Whether the user is active
    is_admin = models.BooleanField(default=False)           # Indicates whether the user is an admin
    created_at = models.DateTimeField(auto_now_add=True)    # Records the creation date and time
    updated_at = models.DateTimeField(auto_now=True)        # Records the last update date and time

    # Custom user manager for this model
    objects = UserManager()

    USERNAME_FIELD = "email"             # Field used for authentication (email instead of username)
    REQUIRED_FIELDS = ["name", "tc"]     # Additional fields required when creating a user

    def __str__(self):
        return self.email               # Return the user's email address as a string

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
