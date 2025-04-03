def mask_account_card(account_info: str) -> str:
    """Функция возвращает строку с замаскированным номером карты или счета"""
    parts = account_info.rsplit(" ", 1)
    account_or_card_number = parts[-1]
    if len(account_or_card_number) == 16:
        return (
            f"{parts[0]} {account_or_card_number[:4]} {account_or_card_number[4:6]}** "
            f"**** {account_or_card_number[-4:]}"
        )
    else:
        return f"{parts[0]} ** {account_or_card_number[-4:]}"


def get_date(date: str) -> str:
    """Функция принимает строку вида 'YYYY-MM-DDTHH:MM:SS.ssssss' и возвращает в формате 'ДД.ММ.ГГГГ"""
    year, month, day = date.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
