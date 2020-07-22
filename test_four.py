"""Тест типа данных Task."""

from collections import namedtuple

import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# pytest -l - при неудачном тесте будут отображаться локальные переменные
# pytest --maxfail=2 --tb=no - аксимальное клоичество сбоев
# pytest -x - проверка остановится после первого проваленного теста
# pytest -v -m run_these_please - запустить тесты с маркой. Пример марки: @pytest.mark.run_these_please
# pytest -v -k "asdict or defaults" - проходит выбранные тесты и показывает результат. (test_asdict и test_defaults)
# pytest --collect-only - показывает функции из файлов
# pytest -v test_four.py - для получения еще больше описаний разлиций
# pytest -q - для сокращения описания
# pytest test_four.py::test_asdict - для запуска только одной функции
def test_asdict():
    """_asdict() должен возвращать словарь."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """должно изменить переданное в fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
