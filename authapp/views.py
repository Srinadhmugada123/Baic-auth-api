from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Creates a new user. Will return 201 if the user was created, or 400 if the user
        could not be created.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "user": serializer.data,
                "message": "user created succesfully"
            }, status=status.HTTP_201_CREATED
            ) 
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
        )


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Handles user login. It will return 200 if the user was logged in, or 401 if the user
        could not be logged in.
        """
        # serializer = RegisterSerializer.objects.all()
        username = request.data.get('username')
        # email = request.data.get(email)
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({
                "user": user.username,
                "email": "user.email",
                "message": "Login successfully",
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "login failed",
            "errors": "Invalid credentials",
        }, status=status.HTTP_401_UNAUTHORIZED)
    

class LogoutAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Handles user logout. It will return 200 if the user was logged out, or 400 if the user
        could not be logged out.
        """
        return Response({
            "message": "Logout successfully"
        })        