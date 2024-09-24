from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.

# class RegisterView(APIView):
#     def post(self, request):
#         if request.POST:
#             username = request.POST['username']
#             password = request.POST['password']
#         elif request.data:
#             username = request.data['username']
#             password = request.data['password']
#         else:
#             return Response('Вы не отправили необходимые данные', status=422)
#         user = User(username=username)
#         user.set_password(password)
#         user.save()
#
#
#         return Response('Вы успешно зарегистрировались', )

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request,*args,**kwargs):
        user_serializer = self.get_serializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response(UserSerializer(user).data)
        return Response(user_serializer.errors, status=422)

class UserGet(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = None

    def get_object(self):
        return self.request.user

class UpdateUserAPIView(APIView):
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=422)

class GetAllUsersAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class GetUserAndNotesAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)