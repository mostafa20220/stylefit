from .models import Profile

class MongoEngineBackend:
    """Custom authentication backend for MongoEngine."""

    def authenticate(self, request, username=None, password=None):
        """Authenticates user from MongoDB"""
        try:
            user = Profile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Retrieve user by ID"""
        try:
            return Profile.objects.get(id=user_id)
        except Profile.DoesNotExist:
            return None
