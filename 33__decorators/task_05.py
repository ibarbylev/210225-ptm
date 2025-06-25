"""Создайте декоратор, которые задваивает гласные буквы в тексте
и переводит их верхний регистр.
(список гласных в русском и английском:
vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ' )

Пример:
"Привет, как дела?"

ПрИИвЕЕт, кААк дЕЕлАА?
"""


def double_uppercase_vowels(func):
    pass


@double_uppercase_vowels
def get_text():
    return "Привет, как дела?"

print(get_text())
