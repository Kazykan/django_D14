from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


# регистрируем наши модели для перевода


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('headingPost', 'textPost',)
