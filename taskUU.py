from collections import Counter

def find_duplicate_words(text):
    # Приводим текст к нижнему регистру и разбиваем на слова
    words = text.lower().split()
    
    # Используем Counter для подсчета вхождений слов
    word_counts = Counter(words)
    
    # Находим и выводим дубликаты
    duplicates = {word: count for word, count in word_counts.items() if count > 1}
    
    return duplicates

# Пример использования
text = "Это пример текста с некоторыми словами. Это текст с дубликатами."
duplicates = find_duplicate_words(text)
print(duplicates)
