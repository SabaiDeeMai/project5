from typing import Dict, List
import pandas as pd
import csv
import logging
import os

os.makedirs('../logs', exist_ok=True)


def setup_logger(name, log_file, level=logging.INFO):
    """Настройка индивидуального логгера для каждого модуля"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    return logger


csv_transactions_logger = setup_logger("csv_transactions", '../logs/csv_transactions.log')
excel_transactions_logger = setup_logger("excel_transactions", '../logs/excel_transactions.log')


def get_read_csv_transact(csv_path: str) -> list[dict]:
    """
    Функция принимает файл CSV и возвращает список словарей
    """
    transact_list = []
    with open(csv_path) as file:
        reader = csv.DictReader(file, delimiter=';')
        csv_transactions_logger.info(f"Файл получен {csv_path}")
        for row in reader:
            my_dict = {"id": row['id'], "state": row["state"], "date": row["date"],
                       "amount": row["amount"], "currency_name": row["currency_name"],
                       "currency_code": row["currency_code"], "from": row["from"], "to": row["to"],
                       "description": row["description"]}
            transact_list.append(my_dict)
        csv_transactions_logger.info("Функция завершена")
    return transact_list


def get_read_excel_transact(excel_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из XLSX-файла и возвращает список словарей.
    """
    transact_excel = []

    try:
        df = pd.read_excel(excel_path, dtype=str, engine="openpyxl")
        excel_transactions_logger.info(f"Успешно загружен файл: {excel_path}")

        if df.empty:
            excel_transactions_logger.warning("Файл не содержит данных")
            return transact_excel

        transact_excel = df.to_dict(orient='records')
        excel_transactions_logger.info(f"Успешно обработано {len(transact_excel)} записей")

        return transact_excel

    except FileNotFoundError:
        excel_transactions_logger.error(f"Файл не найден: {excel_path}")
    except pd.errors.EmptyDataError:
        excel_transactions_logger.error(f"Файл не содержит данных: {excel_path}")
    except Exception as ex:
        excel_transactions_logger.error(f"Ошибка при обработке файла: {str(ex)}", exc_info=True)

    return transact_excel


# excel_transact_new = get_read_excel_transact('../data/transactions_excel.xlsx')
# csv_transact_new = get_read_csv_transact('../data/transactions.csv')
