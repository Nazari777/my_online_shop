from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')


admin.site.register(Member, MemberAdmin)


