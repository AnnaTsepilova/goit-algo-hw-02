import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()


# Функція для генерування нових заявок
def generate_request():
    # Створення унікального ідентифікатору для заявки
    request_id = random.randint(1, 1000)
    request_data = f"Заявка #{request_id}"
    print(f"Створено заявку: {request_data}")
    # Додавання заявки до черги
    request_queue.put(request_data)


# Функція для обробки заявок
def process_request():
    # Якщо черга не порожня
    if not request_queue.empty():
        # Видалення заявки з черги
        request_data = request_queue.get()
        # Обробка заявки
        print(f"Обробка {request_data}...")
        # Імітація часу на обробку
        time.sleep(1)
        print(f"{request_data} оброблено!")
    else:
        # Виведення повідомлення про порожню чергу
        print("Черга пуста, немає заявок для обробки.")


# Основний цикл програми
try:
    while True:
        # Генерація нових заявок з випадковою частотою
        if random.random() > 0.5:  # 50% шанс генерування нової заявки
            generate_request()

        # Обробка заявок у черзі
        process_request()

        # Затримка для імітації реального часу
        time.sleep(2)

except KeyboardInterrupt:
    print("\nПрограма завершена.")
