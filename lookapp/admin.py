from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from lookapp.models import Kasbiy_Standart, Kasbiy_Standart_Atamalari, Kasbiy_Standart_Huquqiy_Hujjat, Category


# Register your models here.

class StandartAdmin(admin.ModelAdmin):
    pass


class Standart_AtamalarAdmin(admin.ModelAdmin):
    pass


class Standart_Huquqiy_HujjatiAdmin(admin.ModelAdmin):
    pass


class CategorieAdmin(admin.ModelAdmin):
    pass


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Kasbiy_Standart, StandartAdmin)
admin.site.register(Kasbiy_Standart_Atamalari, Standart_AtamalarAdmin)
admin.site.register(Kasbiy_Standart_Huquqiy_Hujjat, Standart_Huquqiy_HujjatiAdmin)