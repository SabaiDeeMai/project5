import json
import logging
import os
from typing import Dict, List

os.makedirs('../logs', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('../logs/utils.log', mode='w', encoding='utf-8'),
    ]
)

utils_logger = logging.getLogger("utils_log")
# utils_logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
# file_handler.setFormatter(formatter)
# utils_logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            utils_logger.info(f"Файл получен: {file_path}")
            if isinstance(data, list):
                utils_logger.info("Результат работы функции load_transactions получен")
                return data
            utils_logger.debug("Файл пустой")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        utils_logger.error("Файл не найден")
        return []
