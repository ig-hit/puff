from django.contrib import admin
from django.contrib.auth import admin as auth_admin, forms as auth_forms

from user import models


@admin.register(models.AppUser)
class AppUserAdmin(auth_admin.UserAdmin):
    class CreateForm(auth_forms.UserCreationForm):
        class Meta:
            model = models.AppUser
            fields = ('email',)
            field_classes = {'email': auth_forms.UsernameField}

    ordering = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (None, {
            'fields': ('is_active',),
        }),
        (None, {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2'),
    }),)

    filter_horizontal = ()
    list_filter = ('is_active',)
    search_fields = ('id',)
    list_display = (
        'id',
        'email',
    )
