from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsSuperAdminPermission, IsAdminPermission


# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsSuperAdminPermission, IsAdminPermission)
    renderer_classes = (JSONRenderer,)
    search_fields = ('username', 'email')
    filter_fields = ('username', 'is_superuser', 'email', 'is_active')

