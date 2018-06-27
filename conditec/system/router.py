from conditec.system.api import user

routers = [
    (r'system/users', user.UserViewSet),
    (r'system/groups', user.GroupViewSet),
]