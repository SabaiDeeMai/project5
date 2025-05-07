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


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if card_number.isdigit():
        masks_logger.debug(f"получен номер карты {card_number}")
        masks_logger.debug("Функция завершена")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        masks_logger.error("Номер состоит не из цифр")
        return ''


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if account_number.isdigit():
        masks_logger.debug(f"получен номер счета {account_number}")
        masks_logger.debug("Функция завершена")
        return f"** {account_number[-4:]}"
    else:
        masks_logger.error("Номер счета состоит не из цифр")
        return ''


if __name__ == "__main__":
    print(get_mask_account(str(73654108430135874305)))
    print(get_mask_card_number(str(7000792289606361)))
