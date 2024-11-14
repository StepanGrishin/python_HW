import re
from collections import Counter

def count_unique_words(text: str) -> int:
    # Удаляем все знаки препинания, оставляя только буквы и цифры
    clean_text = re.sub(r'[^\w\s]', '', text)
    
   
    words = clean_text.lower().split()
    
    # Используем Counter для подсчёта уникальных слов
    word_count = Counter(words)
    
    return len(word_count)

# Пример использования:
text = "Привет, как твои делишки? Где деньги?"
unique_words_count = count_unique_words(text)
print(f"Количество уникальных слов: {unique_words_count}")
