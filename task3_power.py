"""Задание 3. Возведение числа A в целую положительную степень N с помощью цикла (без оператора возведения в степень)."""

from __future__ import annotations

import math
from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int, read_number, require_int


def power_by_loop(base: int | float, exponent: int) -> int | float:
    """Вычисляет A в степени N с помощью цикла умножения без использования оператора возведения в степень."""
    if isinstance(base, bool) or not isinstance(base, (int, float)):
        raise TypeError("Основание A должно быть числом.")
    if isinstance(base, float) and not math.isfinite(base):
        raise ValueError("Основание A должно быть конечным числом.")
    require_int(exponent, name="Степень N", min_value=1)

    result: int | float = 1
    for _ in range(exponent):
        result *= base
    return result


def run(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int | float:
    """Запрашивает число A и положительную степень N, выводит результат A^N и возвращает его."""
    base = read_number("Введите число A: ", input_fn=input_fn, output_fn=output_fn)
    exponent = read_int(
        "Введите целую положительную степень N: ",
        min_value=1,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    result = power_by_loop(base, exponent)
    output_fn(f"{base} ^ {exponent} = {result}")
    return result


def main() -> None:
    """Точка входа для Задания 3."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
