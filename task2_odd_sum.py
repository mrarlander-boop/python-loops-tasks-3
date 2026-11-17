"""Задание 2. Вычисление суммы всех нечётных чисел от 1 до 100."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio, require_int

DEFAULT_START = 1
DEFAULT_END = 100


def sum_odd_numbers(start: int = DEFAULT_START, end: int = DEFAULT_END) -> int:
    """Вычисляет сумму всех нечётных чисел в диапазоне [start, end] с помощью цикла."""
    require_int(start, name="Начало диапазона")
    require_int(end, name="Конец диапазона")
    if start > end:
        raise ValueError("Начало диапазона не может быть больше конца.")

    total = 0
    for number in range(start, end + 1):
        if number % 2 != 0:
            total += number
    return total


def run(output_fn: Callable[[str], None] = print) -> int:
    """Выводит сумму всех нечётных чисел от 1 до 100."""
    total = sum_odd_numbers(DEFAULT_START, DEFAULT_END)
    output_fn(f"Сумма всех нечётных чисел от {DEFAULT_START} до {DEFAULT_END}: {total}")
    return total


def main() -> None:
    """Точка входа для Задания 2."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
