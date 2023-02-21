from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.text import gettext_lazy as _

# Register your models here.
from .models import User


class DRFUserAdmin(UserAdmin):
    """
    Overrides UserAdmin
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser',
                                       'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'joined_date',
                                           'update_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile', 'password1',
                       'password2'),
        }),
    )
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'username', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email', 'mobile', 'username', )
    readonly_fields = ('joined_date', 'last_login', 'update_date')


admin.site.register(User, DRFUserAdmin)
