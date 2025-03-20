from django.contrib.auth.models import BaseUserManager
from mongoengine import Document, StringField, EmailField, DateTimeField
from django.utils.timezone import now
import bcrypt


class Profile(Document):
    username = StringField(max_length=50, required=True)
    gender = StringField(max_length=10, required=True)
    email = EmailField(max_length=50, required=True, unique=True)
    password = StringField(
        max_length=250, required=True
    )  # Store hashed passwords securely
    created_at = DateTimeField(default=now)
    updated_at = DateTimeField(default=now)

    def set_password(self, password):
        self.password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self):
        return self.username


class ProfileManager(BaseUserManager):
    """Custom manager to handle user creation"""

    def create_user(self, username, email, password=None):
        """Create and return a regular user"""
        if not email:
            raise ValueError("Users must have an email address")

        user = Profile(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
