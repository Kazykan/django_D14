from django import template


register = template.Library()

forbidden_words = ['ху', 'пиз', 'гон', 'пиз', 'Ху']


@register.simple_tag(takes_context=True, name='unwanted_text')
def unwanted_text(text):
    """Реализуйте фильтр, который заменяет все буквы кроме первой и последней на «*» у слов из списка «нежелательных».
    Предполагается, что в качестве аргумента гарантированно передается текст, и слова разделены пробелами.
    Можно считать, что запрещенные слова находятся в списке forbidden_words
"""
    words = text.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*" * (len(word)-2) + word[-1])
        else:
            result.append(word)
    return ' '.join(result)