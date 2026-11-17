"""Задание 5. Вывод прямоугольника из символов '*' по заданной ширине и высоте."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int, require_int


def build_rectangle(width: int, height: int, symbol: str = "*") -> list[str]:
    """Строит список строк прямоугольника из символа symbol с помощью вложенных циклов."""
    require_int(width, name="Ширина", min_value=1)
    require_int(height, name="Высота", min_value=1)
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Символ заполнения должен быть строкой длины 1.")

    rows: list[str] = []
    for _ in range(height):
        row_chars: list[str] = []
        for _ in range(width):
            row_chars.append(symbol)
        rows.append("".join(row_chars))
    return rows


def run(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> list[str]:
    """Запрашивает ширину и высоту прямоугольника, выводит его и возвращает строки."""
    width = read_int(
        "Введите ширину прямоугольника: ",
        min_value=1,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    height = read_int(
        "Введите высоту прямоугольника: ",
        min_value=1,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    rows = build_rectangle(width, height)
    for row in rows:
        output_fn(row)
    return rows


def main() -> None:
    """Точка входа для Задания 5."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
