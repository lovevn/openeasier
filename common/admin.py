from django.contrib import admin
from .models import *


@admin.register(CKANInstance)
class CKANInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'api_version',)


@admin.register(DBConfig)
class DBConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'port', 'name', 'user_db', 'password_db',)


@admin.register(DBIgnore)
class DBIgnoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'ignore_type', 'db_config',)

'''
@admin.register(UserSchema)
class UserSchemaAdmin(admin.ModelAdmin):
    list_display = ()
'''
