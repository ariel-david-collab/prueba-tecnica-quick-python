# Author: Ariel David Herrera Ahumada
# Date: 2021-11-06
# Version: 1.0.0

from prueba.apps.apiUsers.models import User
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserViewSet(viewsets.ModelViewSet):
    # The API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all()
    permission_classes_by_action = {
        "create": [IsAuthenticated],
        "list": [AllowAny],
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # update the create method to set the password
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # an necessary step to save the user
        serializer.save()

    def _set_fields_to_instance(self, request, instance):
        # set the fields to the instance
        fields = [
            "document_type_id", 
            "document_number", 
            "first_name", 
            "last_name", 
            "session_active"
            "date_birth", 
            "email", 
            "mobile_phone", 
            "address", 
            "token",
            "city_id", 
        ]

        for field in fields:
            if field in request.data:
                setattr(instance, field, request.data[field])

    def update(self, request, pk=None):
        # update the "update" method to set the password
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self._set_fields_to_instance(request, instance)

        if "password" in request.data:
            instance.set_password(request.data["password"])

        instance.save()

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        # update the "partial_update" method to set the password
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self._set_fields_to_instance(request, instance)

        if "password" in request.data:
            instance.set_password(request.data["password"])

        instance.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        # update the "destroy" to view the user deleted
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance.delete()
        return Response(serializer.data)

    def get_serializer_class(self, *args, **kwargs):
        # Dynamic serializer.Meta.fields based on the action
        serializer_class = UserSerializer
        generic_fields = (
                    "first_name", 
                    "last_name", 
                    "date_birth", 
                    "mobile_phone", 
                    "email", 
                    "password", 
                    "address",
                )
        if self.action == "create":
            serializer_class.Meta.fields = generic_fields
        elif self.action == "list":
            serializer_class.Meta.fields = (
                    "id",
                    "first_name", 
                    "last_name", 
                    "date_birth", 
                    "mobile_phone", 
                    "email", 
                    "address",
                    "city_id",
                    "session_active",
                )
        elif self.action == "retrieve":
            serializer_class.Meta.fields = (
                    "id",
                    "document_type_id",
                    "document_number",
                    "first_name", 
                    "last_name", 
                    "date_birth", 
                    "mobile_phone", 
                    "email", 
                    "address",
                    "city_id",
                    "session_active",
                )
        elif self.action == "update":
            serializer_class.Meta.fields = generic_fields
        elif self.action == "partial_update":
            serializer_class.Meta.fields = generic_fields
        elif self.action == "destroy":
            serializer_class.Meta.fields = generic_fields
        return serializer_class

    def get_permissions(self):
        # set the permissions based on the action
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
