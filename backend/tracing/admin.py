from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):

    list_display = (
        'qr_code_text',
        '__str__',
        'email',
        'gender',
        'birthdate',
        'mobile1',
        'mobile2',
        'time_created',
        'time_updated',
    )

    list_filter = (
        ('mobile1_confirmed', admin.BooleanFieldListFilter),
        ('mobile2_confirmed', admin.BooleanFieldListFilter),
    )

    readonly_fields = (
        'qr_code_text',
        'time_created',
        'time_updated',
    )

    search_fields = (
        'lname', 
        'fname', 
        'email',
    )

    ordering = ('lname', )

    fieldsets = (
        ('Basic Info', {'fields': ('qr_code_text', 'fname', 'mname', ('lname', 'ename') , 'gender', 'birthdate',)}),
        ('Contact Info', {'fields': ('email', ('mobile1', 'mobile1_confirmed') , ('mobile2', 'mobile2_confirmed'),)}),
        ('Current Address', {'fields': (('current_street','current_town','current_city', 'current_region',),)}),
        ('Permanent Address', {'fields': (('perm_street','perm_town','perm_city', 'perm_region',),)}),
        ('Identification', {'fields': ('face_photo','id_photo',)}),
        ('Others', {'fields': ('time_created','time_updated',)}),
    )

@admin.register(models.EstablishmentProfileModel)
class EstablishmentProfileModelAdmin(admin.ModelAdmin):
    
    list_display = (
        'establishment_name',
        'email',
        'time_created',
        'time_updated',
    )

    readonly_fields = (
        'time_created',
        'time_updated',
    )

    search_fields = ( 
        'email',
        'establishment_name'
    )

    ordering = ('establishment_name', )

    fieldsets = (
        (None, {'fields': ('establishment_name', )}),
        ('Contact Info', {'fields': ('email', ('mobile1', 'mobile1_confirmed') , ('mobile2', 'mobile2_confirmed'), ('landline', 'landline_confirmed'),)}),
        ('Address', {'fields': (('street','town','city', 'region',),)}),
        ('Others', {'fields': ('time_created','time_updated',)}),
    )
@admin.register(models.TracingModel)
class TracingModelAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'establishment_profile',
        'transact',
        'transact_time',
    )

    readonly_fields = (
        'transact_time',
    )

    # search_fields = ( 
    #     'user_profile__lname',
    #     'user_profile__fname',
    #     'user_profile__email',
    #     'establishment_profile__establishment_name',
    # )
    
    ordering = ('id', )

    fieldsets = (
        (None, {'fields': ('user_profile', 'establishment_profile', 'transact', 'transact_time')}), 
    )