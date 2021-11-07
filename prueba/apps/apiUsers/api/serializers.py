# Author: Ariel David Herrera Ahumada
# Date: 2021-11-06
# Version: 1.0.0

from rest_framework import serializers
from prueba.apps.apiUsers.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                    "first_name", 
                    "last_name", 
                    "date_birth", 
                    "mobile_phone", 
                    "email", 
                    "password", 
                    "address"
                )
