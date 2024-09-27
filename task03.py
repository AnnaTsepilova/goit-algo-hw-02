def check_delimiters(input_str):
    # Стек для зберігання відкритих дужок
    stack = []

    # Словник відповідних пар дужок
    brackets = {')': '(', ']': '[', '}': '{'}

    # Перебір кожного символу у рядку
    for char in input_str:
        # Якщо це відкрита дужка, додаємо її в стек
        if char in brackets.values():
            stack.append(char)
        # Якщо це закрита дужка
        elif char in brackets.keys():
            # Перевіряємо чи є відкриті дужки в стеку та
            # чи співпадає остання відкрита дужка
            if stack and stack[-1] == brackets[char]:
                stack.pop()  # Якщо пара правильна, видаляємо зі стека
            else:
                return "Несиметрично"  # Якщо ні, то дужки несиметричні

    # Якщо стек порожній після перевірки — всі дужки симетричні
    return "Симетрично" if not stack else "Несиметрично"


# Приклади використання
test_str1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
test_str2 = "( 23 ( 2 - 3);"
test_str3 = "( 11 }"

print(f'{test_str1}: {check_delimiters(test_str1)}')
print(f'{test_str2}: {check_delimiters(test_str2)}')
print(f'{test_str3}: {check_delimiters(test_str3)}')
