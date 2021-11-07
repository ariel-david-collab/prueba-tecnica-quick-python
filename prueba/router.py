from prueba.apps.apiUsers.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", UserViewSet)
