from src.utils import load_transactions
from src.transactions import get_read_csv_transact, get_read_excel_transact
from src.filters import filter_by_description
from typing import List, Dict
from collections import Counter

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def input_status() -> str:
    """
    Запрашивает у пользователя статус транзакций для фильтрации.
    Повторяет запрос, пока не будет введён корректный статус из доступных значений.
    """
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                       f"Доступные для фильтровки статусы: {', '.join(VALID_STATUSES)}\n").strip().upper()
        if status in VALID_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status
        else:
            print(f'Статус операции "{status}" недоступен.')


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """
     Фильтрует список транзакций по заданному статусу.
     """
    return [txn for txn in transactions if txn.get("state") == status]


def sort_transactions(transactions: List[Dict], ascending: bool) -> List[Dict]:
    """
    Сортирует транзакции по дате.
    """
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_rubles(transactions: List[Dict]) -> List[Dict]:
    """
    Фильтрует список транзакций, оставляя только транзакции в рублях.
    """
    for txn in transactions:
        currency = (txn.get("operationAmount", {}).get("currency", {}).get("code") or txn.get("currency_code", "")
                    or txn.get("currency_name", ""))
        txn["__currency_code"] = currency
    return [txn for txn in transactions if txn["__currency_code"] == "RUB"]


def count_transactions_by_category(transactions: List[Dict],
                                   category_counter: Counter = None) -> Counter:
    """
    Функция подсчитывает количество операций для каждой категории, основываясь на поле 'description'
    в каждой транзакции.
    """
    if category_counter is None:
        category_counter = Counter()

    for transaction in transactions:
        description = transaction.get("description", "")
        category_counter[description] += 1

    return category_counter


def print_transactions(transactions: List[Dict]) -> None:
    """
    Выводит список транзакций в читаемом формате.
    """
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    category_count = count_transactions_by_category(transactions)
    print("Количество транзакций по категориям:")
    for category, count in category_count.items():
        print(f"{category}: {count} операций")
    print(f"Всего банковских операций в выборке: {category_count.total()}\n")
    print("\nРаспечатываю итоговый список транзакций...\n")

    for txn in transactions:
        date = txn.get("date", "")[:10]
        desc = txn.get("description", "")
        from_ = txn.get("from", "")
        to = txn.get("to", "")

        amount = txn.get("operationAmount", {}).get("amount") or txn.get("amount", "")
        currency = txn.get("operationAmount", {}).get("currency", {}).get("name") or txn.get("currency_name", "")

        print(f"{date} {desc}")
        if from_ and to:
            print(f"{from_} -> {to}")
        print(f"Сумма: {amount} {currency}\n")


def load_transactions_by_choice(choice: str) -> List[Dict]:
    """
    Загружает транзакции из файла, выбранного пользователем: JSON, CSV или XLSX.
    """
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        return load_transactions("../data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        return get_read_csv_transact("../data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return get_read_excel_transact("../data/transactions_excel.xlsx")


def main():
    """
    Основная логика программы.
    Предлагает пользователю выбрать источник данных, применяет фильтры, сортировку,
    отображает итоговые транзакции или сообщает об отсутствии подходящих записей.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    chosen_method = input()
    transactions = load_transactions_by_choice(chosen_method)

    status = input_status()
    filtered = filter_by_status(transactions, status)

    if input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        filtered = sort_transactions(filtered, ascending=(order == "по возрастанию"))

    if input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower() == "да":
        filtered = filter_rubles(filtered)

    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == "да":
        word = input("Введите слово для поиска в описании: ").strip()
        filtered = filter_by_description(filtered, word)

    print_transactions(filtered)


if __name__ == "__main__":
    main()
