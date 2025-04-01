def filter_by_state(data: list, state="EXECUTED") -> list:
    """Функция фильтрует список словарей по значению ключа 'state'"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, descending=True) -> list:
    """Функция сортирует список словарей по ключу 'date'"""
    return sorted(data, key=lambda x: x["date"], reverse=descending)
