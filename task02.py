from collections import deque


def is_palindrome(input_str):
    # Приведення рядка до нижнього регістру та видалення пробілів
    normalized_str = ''.join(input_str.lower().split())

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(normalized_str)

    # Порівняння символів з початку та кінця черги
    while len(char_deque) > 1:
        # Порівнюємо символи на обох кінцях
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Приклад використання функції
test_str = [
    "Radar",
    "Level",
    "Hello world",
    "Tesla 3",
    "Civic",
    "Madam",
    "N o o n"
]

for test in test_str:
    print(f"'{test}' is a palindrome: {is_palindrome(test)}")
