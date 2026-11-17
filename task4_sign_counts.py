"""Задание 4. Подсчёт количества положительных чисел, отрицательных чисел и нулей среди 10 введённых."""

from __future__ import annotations

from collections.abc import Callable, Iterable

from cli_utils import configure_utf8_stdio, read_int, require_int

NUMBERS_COUNT = 10


def count_signs(numbers: Iterable[int]) -> tuple[int, int, int]:
    """Определяет количество положительных, отрицательных чисел и нулей."""
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        require_int(number, name="Число")
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    return positive_count, negative_count, zero_count


def read_integers(
    count: int = NUMBERS_COUNT,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> list[int]:
    """Последовательно считывает заданное количество целых чисел с клавиатуры."""
    require_int(count, name="Количество чисел", min_value=1)

    numbers: list[int] = []
    for index in range(1, count + 1):
        value = read_int(
            f"Введите целое число ({index} из {count}): ",
            input_fn=input_fn,
            output_fn=output_fn,
        )
        numbers.append(value)
    return numbers


def run(
    count: int = NUMBERS_COUNT,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> tuple[int, int, int]:
    """Запрашивает 10 целых чисел, выводит подсчёт по знакам и возвращает результат."""
    numbers = read_integers(count=count, input_fn=input_fn, output_fn=output_fn)
    positive_count, negative_count, zero_count = count_signs(numbers)
    output_fn(f"Количество положительных чисел: {positive_count}")
    output_fn(f"Количество отрицательных чисел: {negative_count}")
    output_fn(f"Количество нулей: {zero_count}")
    return positive_count, negative_count, zero_count


def main() -> None:
    """Точка входа для Задания 4."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
