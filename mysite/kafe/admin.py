from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from.models import Food, Category, Comment, FoodPhoto,UserProfile, Rating


admin.site.register(Category)
admin.site.register(FoodPhoto)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Rating)


@admin.register(Food)
class BookAdmin(TranslationAdmin):
    list_display = ('name',)
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',)
        }

