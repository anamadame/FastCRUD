from modeltranslation.translator import TranslationOptions, register
from .models import Food


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'category', 'description')