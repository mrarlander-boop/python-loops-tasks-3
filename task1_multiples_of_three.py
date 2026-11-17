"""Задание 1. Вывод всех чисел от 1 до N, кратных трём."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int, require_int


def find_multiples_of_three(n: int) -> list[int]:
    """Находит все числа от 1 до N включительно, делящиеся на 3 без остатка."""
    require_int(n, name="N", min_value=1)

    multiples: list[int] = []
    for number in range(1, n + 1):
        if number % 3 == 0:
            multiples.append(number)
    return multiples


def run(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> list[int]:
    """Запрашивает N и выводит все числа от 1 до N, кратные 3."""
    n = read_int(
        "Введите целое положительное число N: ",
        min_value=1,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    multiples = find_multiples_of_three(n)
    if not multiples:
        output_fn(f"В диапазоне от 1 до {n} нет чисел, кратных 3.")
        return multiples

    output_fn(f"Числа от 1 до {n}, кратные 3:")
    for number in multiples:
        output_fn(str(number))
    return multiples


def main() -> None:
    """Точка входа для Задания 1."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
