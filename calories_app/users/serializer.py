from rest_framework import serializers
from rest_auth import serializers as auth_serializers
from rest_auth.models import TokenModel

from .models import User


class UserDetailsSerializer(auth_serializers.UserDetailsSerializer):
    """
    User Details Serializer
    """
    # permissions = serializers.SerializerMethodField('get_user_role_permissions')

    class Meta:
        model = User
        fields = ('pk', 'username',
                  'first_name', 'last_name',
                  'email', 'mobile',
                  'joined_date', 'update_date',
                  'is_active', 'is_staff')
        read_only_fields = ('username',)
        ref_name = 'User'

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

    # def get_user_role(self, instance):
    #     """
    #     This method gets particular user role.
    #     """
    #     role = {
    #         "id": instance.role.id,
    #         "role_name": instance.role.role_name,
    #         "is_active": instance.role.is_active,
    #         "created": instance.role.created,
    #         "modified": instance.role.modified
    #     }
    #
    #     return role
    #
    # def get_master_role_details(self, instance):
    #     """
    #     This method gets particular role's master-role details.
    #     """
    #     master_role = {
    #         "id": instance.role.master_role.id,
    #         "master_role": instance.role.master_role.master_role,
    #         "is_active": instance.role.master_role.is_active,
    #         "created": instance.role.master_role.created,
    #         "modified": instance.role.master_role.modified
    #     }
    #     return master_role
    #
    # def get_user_role_permissions(self, instance):
    #     """
    #     This method gets particular role's permissions that are active.
    #     """
    #     permissions = instance.role.permissions.all()
    #     perm_list = []
    #     for perm in permissions:
    #         if perm.is_active:
    #             perm_list.append(perm.permission_name)
    #
    #     return perm_list


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user',)
