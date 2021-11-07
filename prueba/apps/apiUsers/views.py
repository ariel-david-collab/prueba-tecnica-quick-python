# Author: Ariel David Herrera Ahumada
# Date: 2021-11-06
# Version: 1.0.0

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # according to the docs (Prueba Tecnica for Quick), only the access_token, and token_type are returned
        del data["refresh"]
        del data["access"]
        refresh = self.get_token(self.user)
        self.user.token = refresh.access_token
        self.user.save()

        data_set = {
            "id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "session_active": self.user.session_active,
            "date_birth": self.user.date_birth,
            "email": self.user.email,
            "mobile_phone": self.user.mobile_phone,
            "password": self.user.password,
            "address": self.user.address,
        }
        # set to the json the user data
        data["user"] = data_set

        data["access_token"] = str(self.user.token)
        data["token_type"] = "bearer"


        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
