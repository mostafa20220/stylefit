from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import jwt
import datetime
from django.conf import settings
from .models import Profile
from .serializers import ProfileSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        gender = request.data.get("gender")

        if Profile.objects(username=username).first():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = Profile(username=username, email=email, gender=gender)
        user.set_password(password)  # Hash password
        user.save()

        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = Profile.objects(username=username).first()
        if user and user.check_password(password):
            # Generate JWT token
            payload = {
                "id": str(user.id),
                "exp": datetime.datetime.now(datetime.timezone.utc)
                + datetime.timedelta(days=20),
                "iat": datetime.datetime.now(datetime.timezone.utc),
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

            # PyJWT in newer versions returns bytes instead of string, so decode if needed
            if isinstance(token, bytes):
                token = token.decode("utf-8")

            return Response({"token": token}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class ProfileView(APIView):
    def get(self, request):
        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return Response(
                {"error": "No valid token provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token = auth_header.split(" ")[1]

        try:
            # Decode token and get user
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = Profile.objects.get(id=payload["id"])
            request.user = user
        except (jwt.ExpiredSignatureError, jwt.DecodeError, Profile.DoesNotExist):
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
