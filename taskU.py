# Напишите программу, которая принимает текст и выводит два слова: 
# наиболее часто встречающееся и самое длинное.
from collections import Counter

text = 'an apple is larger than an apricot'

words = text.lower().split()
word_counts = Counter(words)

duplicates = {word: count for word, count in word_counts.items() if count > 1}

print(duplicates)
