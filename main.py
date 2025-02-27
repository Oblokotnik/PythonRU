print("Creators: SEI163 and Keny")
print("Telegram channel: @Coin_Ts")
import re

# Словарь соответствий английских ключевых слов русским
russian_keywords = {
    "печать": "print",
    "если": "if",
    "иначе": "else",
    "для": "for",
    "пока": "while",
    "функция": "def",
    "вернуть": "return",
    "истина": "True",
    "импортировать": "import",
    "ложь": "False",
    "ничего": "None",
    "класс": "class",
    "продолжить": "continue",
    "прервать": "break",
    "попытка": "try",
    "исключение": "except",
    "поднять": "raise",
    "импорт": "import",
    "как": "as",
    "из": "from",
    "глобальный": "global",
    "не": "not",
    "и": "and",
    "или": "or",
    "в": "in",
    "есть": "is",
    "лямбда": "lambda",
    "с": "with",
    "асинхронный": "async",
    "ждать": "await",
    "урожай": "yield",
    "нелокальный": "nonlocal",
    "удалить": "del",
    "утверждать": "assert",
    "проходить": "pass",
    "показывать": "show",
    "читать": "read",
    "писать": "write",
    "диапазон": "range",
    "запомнить": "save"
}

def translate_to_python(russian_code):
    string_literals = re.findall(r'(".*?")|(\'.*?\')', russian_code)
    replacements = {}
    for i, match in enumerate(string_literals):
        if match[0]: 
            replacements[f"string_{i}"] = match[0]
            russian_code = russian_code.replace(match[0], f"string_{i}")
        elif match[1]:
            replacements[f"string_{i}"] = match[1]
            russian_code = russian_code.replace(match[1], f"string_{i}")

    for russian, english in russian_keywords.items():
        russian_code = re.sub(r'\b' + russian + r'\b', english, russian_code)
    for i in range(len(string_literals)):
        russian_code = russian_code.replace(f"string_{i}", replacements[f"string_{i}"])

    return russian_code

def execute_russian_code(russian_code):
    python_code = translate_to_python(russian_code)
    try:
        exec(python_code)
    except Exception as e:
        print(f"Ошибка выполнения: {e}")

# код
russian_code = """
# Это пример кода на русском Python
функция приветствие(имя):
    печать("Привет, " + имя + "!")

если name == "main":
    имя = "Мир"
    приветствие(имя)

    для i в диапазон(5):
        печать("Число:", i)

    пока i < 10:
        печать("i меньше 10:", i)
        i = i + 1

    если i есть ничего:
        печать("i есть ничего")
    иначе:
        печать("i не есть ничего")

"""
