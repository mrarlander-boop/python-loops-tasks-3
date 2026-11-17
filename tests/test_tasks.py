"""Модульные тесты для пяти практических заданий по циклам (часть 3)."""

from __future__ import annotations

import ast
import sys
import unittest
from collections.abc import Callable
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import cli_utils
import main as menu_main
import task1_multiples_of_three
import task2_odd_sum
import task3_power
import task4_sign_counts
import task5_rectangle


def make_io(
    inputs: list[str],
) -> tuple[Callable[[str], str], Callable[[str], None], list[str]]:
    """Создаёт моки ввода-вывода и журнал сообщений для тестирования CLI."""
    iterator = iter(inputs)
    outputs: list[str] = []

    def fake_input(prompt: str) -> str:
        outputs.append(prompt)
        return next(iterator)

    def fake_output(message: str) -> None:
        outputs.append(message)

    return fake_input, fake_output, outputs


class TestCliUtils(unittest.TestCase):
    """Тесты вспомогательных функций ввода и проверки чисел."""

    def test_read_number_supports_int_dot_and_comma(self) -> None:
        fake_input, fake_output, outputs = make_io(["abc", "nan", "inf", "2,5", "-7"])
        first = cli_utils.read_number("A: ", input_fn=fake_input, output_fn=fake_output)
        second = cli_utils.read_number("A: ", input_fn=fake_input, output_fn=fake_output)
        self.assertIsInstance(first, float)
        self.assertAlmostEqual(first, 2.5)
        self.assertIsInstance(second, int)
        self.assertEqual(second, -7)
        self.assertIn("Ошибка: введите корректное число.", outputs)
        self.assertIn("Ошибка: введите конечное число.", outputs)


class TestTask1MultiplesOfThree(unittest.TestCase):
    """Тесты Задания 1 (числа от 1 до N, кратные 3)."""

    def test_find_multiples_of_three(self) -> None:
        self.assertEqual(task1_multiples_of_three.find_multiples_of_three(10), [3, 6, 9])
        self.assertEqual(task1_multiples_of_three.find_multiples_of_three(2), [])
        with self.assertRaises(ValueError):
            task1_multiples_of_three.find_multiples_of_three(0)

    def test_run_handles_empty_and_non_empty(self) -> None:
        fake_input, fake_output, outputs = make_io(["2"])
        self.assertEqual(task1_multiples_of_three.run(input_fn=fake_input, output_fn=fake_output), [])
        self.assertIn("В диапазоне от 1 до 2 нет чисел, кратных 3.", outputs)

        fake_input, fake_output, outputs = make_io(["0", "9"])
        result = task1_multiples_of_three.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(result, [3, 6, 9])
        self.assertEqual(outputs[-3:], ["3", "6", "9"])


class TestTask2OddSum(unittest.TestCase):
    """Тесты Задания 2 (сумма нечётных чисел от 1 до 100)."""

    def test_sum_odd_numbers_1_to_100(self) -> None:
        self.assertEqual(task2_odd_sum.sum_odd_numbers(), 2500)

    def test_run_outputs_sum(self) -> None:
        outputs: list[str] = []
        total = task2_odd_sum.run(output_fn=outputs.append)
        self.assertEqual(total, 2500)
        self.assertEqual(outputs, ["Сумма всех нечётных чисел от 1 до 100: 2500"])


class TestTask3Power(unittest.TestCase):
    """Тесты Задания 3 (возведение в степень без оператора **)."""

    def test_power_by_loop_int_and_float(self) -> None:
        self.assertEqual(task3_power.power_by_loop(2, 5), 32)
        self.assertEqual(task3_power.power_by_loop(-3, 3), -27)
        self.assertEqual(task3_power.power_by_loop(0, 4), 0)
        self.assertAlmostEqual(task3_power.power_by_loop(1.5, 3), 3.375)

    def test_power_rejects_invalid_inputs_and_does_not_use_pow_operator(self) -> None:
        with self.assertRaises(ValueError):
            task3_power.power_by_loop(2, 0)
        with self.assertRaises(TypeError):
            task3_power.power_by_loop(True, 2)

        source = (PROJECT_ROOT / "task3_power.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        pow_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Pow)]
        self.assertEqual(pow_nodes, [])

    def test_run_interactive(self) -> None:
        fake_input, fake_output, outputs = make_io(["2", "0", "4"])
        result = task3_power.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(result, 16)
        self.assertIn("2 ^ 4 = 16", outputs)


class TestTask4SignCounts(unittest.TestCase):
    """Тесты Задания 4 (подсчёт положительных, отрицательных и нулей)."""

    def test_count_signs(self) -> None:
        stats = task4_sign_counts.count_signs([5, -1, 0, 12, -9, 0, 3, 7, -4, 0])
        self.assertEqual(stats, (4, 3, 3))

    def test_count_signs_rejects_bool(self) -> None:
        with self.assertRaises(TypeError):
            task4_sign_counts.count_signs([1, False, -1])

    def test_run_reads_ten_numbers_with_validation(self) -> None:
        inputs = ["-3", "bad", "0", "4", "0", "-2", "8", "1", "-9", "0", "6"]
        fake_input, fake_output, outputs = make_io(inputs)
        stats = task4_sign_counts.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(stats, (4, 3, 3))
        self.assertIn("Количество положительных чисел: 4", outputs)
        self.assertIn("Количество отрицательных чисел: 3", outputs)
        self.assertIn("Количество нулей: 3", outputs)


class TestTask5Rectangle(unittest.TestCase):
    """Тесты Задания 5 (прямоугольник из символов *)."""

    def test_build_rectangle_5x3(self) -> None:
        self.assertEqual(
            task5_rectangle.build_rectangle(5, 3),
            ["*****", "*****", "*****"],
        )

    def test_invalid_dimensions_raise(self) -> None:
        with self.assertRaises(ValueError):
            task5_rectangle.build_rectangle(0, 3)
        with self.assertRaises(ValueError):
            task5_rectangle.build_rectangle(5, -1)

    def test_run_interactive(self) -> None:
        fake_input, fake_output, outputs = make_io(["0", "5", "3"])
        rows = task5_rectangle.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(rows, ["*****", "*****", "*****"])
        self.assertEqual(outputs[-3:], ["*****", "*****", "*****"])


class TestMainMenu(unittest.TestCase):
    """Тесты интерактивного меню."""

    def test_menu_dispatches_and_exits(self) -> None:
        called: list[str] = []
        fake_tasks = {1: ("Тест", lambda: called.append("done"))}
        fake_input, fake_output, outputs = make_io(["7", "1", "0"])
        menu_main.run_menu(input_fn=fake_input, output_fn=fake_output, tasks=fake_tasks)
        self.assertEqual(called, ["done"])
        self.assertIn("Выход из программы.", outputs)


if __name__ == "__main__":
    unittest.main()
