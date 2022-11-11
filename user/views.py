from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework import authentication, generics, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializerAdmin, UserSerializerToken


class TokenCreate(ObtainAuthToken):
    """
    post:
        Creates a new auth token for user. Authentication required.\n
        Token obtained must be used in the header of every request if admin information is required.
    """
    serializer_class = UserSerializerToken
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserCreate(generics.CreateAPIView):
    """
    post:
        Creates a new user/admin. Authentication as admin is required.
        If is_staff is True, user is admin.
    """
    serializer_class = UserSerializerAdmin
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class UserView(viewsets.ModelViewSet):
    """
    list:
        User list. Authentication as admin is required.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    serializer_class = UserSerializerAdmin
    queryset = get_user_model().objects.all()


class UserManage(generics.RetrieveUpdateDestroyAPIView):

    """
    get:
        Return a user by its id. Authentication as admin is required.

    put:
        Update the entire user. Authentication as admin is required.

    patch:
        Partially update of user. Authentication as admin is required.

    delete:
        Delete a user by its id. Authentication as admin is required.
    """
    serializer_class = UserSerializerAdmin
    queryset = ''
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_object(self):
        """ Return a user by its id """
        user = get_object_or_404(get_user_model(), id=self.kwargs['pk'])
        return user

    def delete(self, request, *args, **kwargs):
        """ Delete a user by its id """
        user = get_object_or_404(get_user_model(), id=self.kwargs['pk'])
        user.delete()
        return HttpResponse(status=200)