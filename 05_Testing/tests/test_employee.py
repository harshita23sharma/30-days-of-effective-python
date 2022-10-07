from src.employee import Employee
import pytest

"""
Fixtures
"""


@pytest.fixture
def employee_obj():
    """
    Test Employee Fixture
    """
    obj = Employee(first="Corey", last="Schafer", pay=50000)
    return obj


def test_employee_init(employee_obj):
    employee_obj.first = "Corey"
    employee_obj.last = "Schafer"
    employee_obj.pay = 50000


def test_email(employee_obj):
    assert employee_obj.email == "Corey.Schafer@email.com"


def test_fullname(employee_obj):
    assert employee_obj.fullname == "Corey Schafer"
