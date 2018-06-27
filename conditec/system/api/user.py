from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login,  logout
from rest_framework import serializers, viewsets
from django.http.response import JsonResponse
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def get_user_info(request):
    return JsonResponse({
        "usename":request.user.username,
    })

def logout(request):
    logout(request)
    return JsonResponse({"status":200})

