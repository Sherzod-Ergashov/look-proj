from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeRelatedFieldListFilter

from lookapp.models import Kasbiy_Standart, Kasbiy_Standart_Atamalari, Kasbiy_Standart_Huquqiy_Hujjat, Category, Book, \
    BookAuthor, Auther, Type


# Register your models here.
@admin.register(Type)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Auther)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class BooksAuthorInline(admin.TabularInline):
    model = BookAuthor

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'isbn')
    list_editable = ('isbn',)

    inlines = [BooksAuthorInline]


# class StandartChildAdmin(admin.TabularInline):
#      model = Kasbiy_Standart
#      extra = 1
#      fields = '__all__'

class StandartAdmin(admin.ModelAdmin):
    pass


class Standart_AtamalarAdmin(admin.ModelAdmin):
    list_display = ('atama', 'izoh')
    list_per_page = 2
    list_editable = ['izoh']
    ordering = ['atama',]


class Standart_Huquqiy_HujjatiAdmin(admin.ModelAdmin):
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