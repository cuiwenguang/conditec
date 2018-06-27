from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from rest_framework import serializers, viewsets
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.http.response import JsonResponse


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class GroupViewSet(viewsets.ModelViewSet):
    """用户组，用户角色管理"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups')


class UserViewSet(viewsets.ModelViewSet):
    """
    用户接口：
    1. 获取所有用户
    2. 根据id获取某一个用户,当用户id=0时，获取的是当前用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_object(self):
        id = self.request.GET.get('pk', '0')
        if int(id) == 0:
            # 0 表示获取自己的信息
            try:
                access_token = self.request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                return Token.objects.get(key=access_token).user
            except:
                raise Http404
        return super().get_object()


def logout(request):
    """注销"""
    Token.objects.filter(user=request.user).delete()
    logout(request)
    return JsonResponse({"status":200})

