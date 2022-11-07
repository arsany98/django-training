from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist


class IsArtistOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return request.user.artist is not None
        except ObjectDoesNotExist:
            return False
