import re
from typing import List, Dict


def filter_by_description(transactions: List[Dict], search_term: str) -> List[Dict]:
    """
    Фильтрует список транзакций по совпадению строки поиска с описанием.
    """
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return [txn for txn in transactions if 'description' in txn and pattern.search(txn['description'])]


def count_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций, относящихся к заданным категориям на основе поля 'description'.
    """
    result = {category: 0 for category in categories}
    for txn in transactions:
        desc = txn.get("description", "").lower()
        for category in categories:
            if category.lower() in desc:
                result[category] += 1
    return result
