"""Общие вспомогательные функции для ввода-вывода и проверки числовых значений."""

from __future__ import annotations

import math
import sys
from collections.abc import Callable


def configure_utf8_stdio() -> None:
    """Настраивает стандартные потоки ввода-вывода на кодировку UTF-8, если это поддерживается."""
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        encoding = getattr(stream, "encoding", "") or ""
        if callable(reconfigure) and encoding.lower() != "utf-8":
            reconfigure(encoding="utf-8")


def _format_range_error(
    min_value: int | None,
    max_value: int | None,
    subject: str = "целое число",
) -> str:
    """Формирует сообщение об ошибке при выходе числа за допустимые границы."""
    if min_value is not None and max_value is not None:
        return f"Ошибка: введите {subject} от {min_value} до {max_value}."
    if min_value is not None:
        return f"Ошибка: введите {subject} не меньше {min_value}."
    return f"Ошибка: введите {subject} не больше {max_value}."


def require_int(
    value: int,
    name: str = "Значение",
    min_value: int | None = None,
    max_value: int | None = None,
) -> int:
    """Проверяет, что значение является целым числом (не bool) и входит в заданные границы."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} должно быть целым числом.")
    if (min_value is not None and value < min_value) or (
        max_value is not None and value > max_value
    ):
        raise ValueError(_format_range_error(min_value, max_value, subject=name.lower()))
    return value


def read_int(
    prompt: str,
    min_value: int | None = None,
    max_value: int | None = None,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int:
    """Запрашивает у пользователя целое число с проверкой корректности и границ."""
    while True:
        raw = input_fn(prompt)
        try:
            value = int(raw.strip())
        except ValueError:
            output_fn("Ошибка: введите корректное целое число.")
            continue

        if (min_value is not None and value < min_value) or (
            max_value is not None and value > max_value
        ):
            output_fn(_format_range_error(min_value, max_value))
            continue

        return value


def read_number(
    prompt: str,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int | float:
    """Запрашивает у пользователя целое или вещественное число (с точкой или запятой)."""
    while True:
        normalized = input_fn(prompt).strip().replace(",", ".")
        try:
            return int(normalized)
        except ValueError:
            pass

        try:
            value = float(normalized)
        except ValueError:
            output_fn("Ошибка: введите корректное число.")
            continue

        if not math.isfinite(value):
            output_fn("Ошибка: введите конечное число.")
            continue

        return value
