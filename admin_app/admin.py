from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class AnnonceAdmin(admin.ModelAdmin):
    list_display = ['categorie',
                    'prix', 'date_ajout']
    list_display_links = ['categorie']

    class Meta:
        model = Annonce


admin.site.register(Annonce, AnnonceAdmin)


# class ProfileAdminInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name = 'Profile'

# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileAdminInline,)

# class ProfileAdminInline(admin.ModelAdmin):
#     list_display_links = ['user']

#     class Meta:
#         model = Annonce

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'tel']
    list_display_links = ['user']

    class Meta:
        model = Annonce


#admin.site.unregister(User)
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(User, UserAdmin)
