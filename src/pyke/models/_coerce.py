from collections.abc import Mapping
from typing import Any


def to_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default

    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def to_float(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def to_str(value: Any, default: str = "") -> str:
    if value is None:
        return default

    return str(value)


def to_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value

    if value is None:
        return default

    if isinstance(value, (int, float)):
        return value != 0

    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes", "y", "on"}:
            return True
        if normalized in {"false", "0", "no", "n", "off", ""}:
            return False

    return default


def to_int_list(value: Any) -> list[int]:
    if not isinstance(value, list):
        return []

    result: list[int] = []
    for item in value:
        coerced = to_int(item, default=-1)
        if coerced != -1:
            result.append(coerced)

    return result


def to_str_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []

    return [str(item) for item in value if item is not None]


def to_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value

    if isinstance(value, Mapping):
        return dict(value)

    return {}


def to_dict_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []

    result: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            result.append(item)
        elif isinstance(item, Mapping):
            result.append(dict(item))

    return result
