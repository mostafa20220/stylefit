import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Profile


class JWTAuthentication(BaseAuthentication):
    """Custom authentication class for JWT in MongoDB"""

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None  # No authentication provided

        try:
            # Extract token (Expected format: "Bearer <token>")
            prefix, token = auth_header.split()
            if prefix.lower() != "bearer":
                raise AuthenticationFailed("Invalid token header. Use 'Bearer <token>'")

            # Decode token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("id")

            request.user_id = user_id

            # Retrieve user from MongoDB
            user = Profile.objects(id=user_id).first()

            request.user = user
            if not user:
                raise AuthenticationFailed("User not found")

            return user, None  # Authentication successful

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")
