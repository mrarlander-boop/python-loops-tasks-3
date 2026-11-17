"""Единое интерактивное меню для запуска пяти заданий по циклам (часть 3)."""

from __future__ import annotations

from collections.abc import Callable

import task1_multiples_of_three
import task2_odd_sum
import task3_power
import task4_sign_counts
import task5_rectangle
from cli_utils import configure_utf8_stdio, read_int

TASKS: dict[int, tuple[str, Callable[[], object]]] = {
    1: ("Числа от 1 до N, кратные трём", task1_multiples_of_three.main),
    2: ("Сумма нечётных чисел от 1 до 100", task2_odd_sum.main),
    3: ("Возведение числа A в степень N (без **)", task3_power.main),
    4: ("Подсчёт положительных, отрицательных чисел и нулей", task4_sign_counts.main),
    5: ("Прямоугольник из символов *", task5_rectangle.main),
}


def run_menu(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
    tasks: dict[int, tuple[str, Callable[[], object]]] | None = None,
) -> None:
    """Запускает интерактивное меню выбора заданий до выбора выхода (0)."""
    task_map = tasks if tasks is not None else TASKS

    while True:
        output_fn("\n=== Практические задания по циклам (часть 3) ===")
        for number, (title, _) in task_map.items():
            output_fn(f"{number}. {title}")
        output_fn("0. Выход")

        choice = read_int(
            f"Выберите номер задания (0-{max(task_map)}): ",
            min_value=0,
            max_value=max(task_map),
            input_fn=input_fn,
            output_fn=output_fn,
        )
        if choice == 0:
            output_fn("Выход из программы.")
            return
        if choice not in task_map:
            output_fn("Ошибка: такого задания нет в меню.")
            continue

        _, runner = task_map[choice]
        output_fn("")
        runner()


def main() -> None:
    """Точка входа единого меню."""
    configure_utf8_stdio()
    run_menu()


if __name__ == "__main__":
    main()
