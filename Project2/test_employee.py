import pytest

from employee import Employee

@pytest.fixture #fixture装饰器
def example_employee():
    example_employee=Employee("小明", "张", 150000)
    return example_employee

def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary == 155000

def test_give_custom_raise(example_employee):
    example_employee.give_raise(10000)
    assert example_employee.salary == 160000