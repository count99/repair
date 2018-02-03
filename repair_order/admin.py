from django.contrib import admin
from repair_order.models import Manufacturers, RepairOrders, Pictures
from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group

# admin.site.register(User)
# Register your models here.
# admin.site.register(Manufacturers)
# admin.site.register(RepairOrders)
# admin.site.register(Pictures)


class MyAdminSite(AdminSite):
    site_title = ugettext_lazy('Hoya維修單管理系統')
    site_header = ugettext_lazy('Hoya維修單管理系統')


class PicturesInline(admin.TabularInline):
    model = Pictures


class RepairOrdersAdmin(admin.ModelAdmin):
    inlines = [
        PicturesInline,
    ]


admin_site = MyAdminSite()

admin_site.register(User)
admin_site.register(Group)
admin_site.register(Manufacturers)
admin_site.register(RepairOrders, RepairOrdersAdmin)
admin_site.register(Pictures)
