from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import HttpResponse

from .models import User, Position
from .serializer import UserSerializer


class SignUpView(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer = UserSerializer

    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            first_error = list(serializer.errors)[0]
            print(e)
            return render(request, 'registration/signup.html',
                          {'field': first_error, 'error': serializer.errors[first_error][0]})
        print(serializer.validated_data)
        user = serializer.create(validated_data=serializer.validated_data)

        return HttpResponse("signed up!")


class LoginView(APIView):
    def get(self, request):
        return render(request, "registration/login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return "home"
        else:
            return render(request, "registration/login.html",
                          {"error": "Username or Password isn't correct"})


class PositionsView(APIView):
    def get(self, request):
        return Position.objects.all()


