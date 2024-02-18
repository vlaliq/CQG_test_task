from typing import Dict, List, Tuple
import sys

def read_config_file(file_path: str) -> Dict[str, str]:
    config_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config_dict[key.strip()] = value.strip()
    return config_dict


def read_text_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.readlines()



def replace_values(text: str, replacements: Dict[str, str]) -> Tuple[str, int]:
    """
        Заменяет значения в тексте согласно переданным заменам replacements.
        Args:
            text (str): Исходный текст, в котором происходят замены.
            replacements (Dict[str, str]): Словарь с заменами, где ключи - значения,
                которые нужно заменить, а значения - значения, на которые нужно заменить.
        Returns:
            Tuple[str, int]: Кортеж, содержащий измененный текст и количество замененных символов.
        """
    count = 0
    for line in text.split('\n'):
        for old_value, new_value in replacements.items():
            text = text.replace(old_value, new_value)
            count += line.count(old_value)
    return text, count

def sort_by_replacements(text_lines: List[str], replacements: Dict[str, str]) -> List[str]:
    # Создаем список кортежей (строка, количество замененных символов)
    sorted_lines = [(line, replace_values(line, replacements)[1]) for line in text_lines]
    # Сортируем строки по убыванию количества замененных символов
    sorted_lines.sort(key=lambda x: x[1], reverse=True)
    # Возвращаем только отсортированные строки без количества замененных символов
    return sorted_lines#[line[0] for line in sorted_lines]


def print_text(texts: List[str]):
    for text in texts:
       print(text.strip())

def print_text_with_count(texts: List[str]):
    for text, count in texts:
        print(f"{text.strip()}   Количество измененных символов: {count}")


def main(configuration_file: str, text_file: str):
    # Читаем файлы
    config = read_config_file(configuration_file)
    text_lines = read_text_file(text_file)

    # Запрос выбора действия у пользователя
    print("Выберите действие:")
    print("1 - Заменить значения без сортировки")
    print("2 - Заменить значения с сортировкой")
    choice = input("Введите номер действия: ")

    if choice == "1":
        # Заменяем значения без сортировки
        replaced_texts = [replace_values(line, config)[0] for line in text_lines]
        # Выводим замененные строки на консоль
        print_text(replaced_texts)

    elif choice == "2":
        # Заменяем значения с сортировкой
        sorted_texts = sort_by_replacements(text_lines, config)
        # Выводим отсортированные строки и количество измененных символов на консоль
        print_text_with_count(sorted_texts)

    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task.py <config_file_path> <text_file_path>")
        sys.exit(1)

    configuration_file = sys.argv[1]
    text_file = sys.argv[2]

    main(configuration_file, text_file)