import logging
import os

os.makedirs('../logs', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('../logs/masks.log', mode='w', encoding='utf-8'),
    ]
)

masks_logger = logging.getLogger("masks_log")

# masks_logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding='utf-8')
# file_handler.setFormatter(formatter)
# masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    masks_logger.debug(f"Получение номера карты: {card_number}")
    if card_number.isdigit():
        masks_logger.debug("Результат работы функции get_mask_card_number получен")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        masks_logger.error("Карта состоит не из цифр")
        return ""


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    masks_logger.debug(f"Получение номера карты: {account_number}")
    if account_number.isdigit():
        masks_logger.debug("Результат работы функции get_mask_account получен")
        return f"** {account_number[-4:]}"
    else:
        masks_logger.error("Счет состоит не из цифр")
        return ""


if __name__ == "__main__":
    print(get_mask_account(str(7365410843013587430)))
    print(get_mask_card_number(str(7000792289606361)))
