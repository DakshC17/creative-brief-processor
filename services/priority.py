from utils.constants import PRIORITY_HIGH, PRIORITY_LOW, PRIORITY_MEDIUM


def calculate_priority(deadline: str, number_of_assets: int) -> str:
    days = _extract_days(deadline)

    if days <= 2 or number_of_assets >= 5:
        return PRIORITY_HIGH
    if days <= 5 or number_of_assets >= 3:
        return PRIORITY_MEDIUM
    return PRIORITY_LOW


def _extract_days(deadline: str) -> int:
    import re

    match = re.search(r"\d+", deadline)
    return int(match.group()) if match else 999
