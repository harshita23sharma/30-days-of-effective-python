import pytest
from src.calc import add

# def test_add():
# 	# Arrange
# 	a = 2
# 	b = 5
# 	expected = 7

# 	# Act
# 	output = add(a, b)

# 	# Assert
# 	assert output == expected​

#parametrize takes two args: first as str and second as list of tuples
@pytest.mark.parametrize("a,b,expected",
							[(10, 5, 15),
							(-1, 1, 0),
							(-1, -1, -2)])
def test_add(a, b, expected):
	assert add(a, b) == expected

"""
Run all tests using `python3 -m pytest tests`
"""


# Fixture
# Fixture is a function with decorator that creates a resource and returns it. 
# If you need the same test input for multiple test cases,
# you can use fixture to prepare the arrange step, just as the example below.
@pytest.fixture
def employee_obj_helper():
    """
    Test Employee Fixture
    """
    obj = Employee(first='Corey', last='Schafer', pay=50000)
    return obj

def test_employee_init(employee_obj):
    employee_obj.first = 'Corey'
    employee_obj.last = 'Schafer'
    employee_obj.pay = 50000

def test_email(employee_obj):
    assert employee_obj.email == 'Corey.Schafer@email.com'

def test_fullname(employee_obj):
    assert employee_obj.fullname == 'Corey Schafer'
