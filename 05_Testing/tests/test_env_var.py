"""
nvironment Variable (monkeypatch.setenv)
Sometimes tests require environment setup, which could be a database connection, a network access or environment variable setup.

The monkeypatch fixture helps you to safely set/delete an attribute, dictionary item or environment variable, or to modify sys.path for importing.
"""

import pytest
from src.env_var import use_env_var


@pytest.mark.parametrize(
    "mock_contract_class,expect",
    [("en_cloud", "this is en_cloud"), ("en_onprem", "this is en_onprem")],
)
def test_mock_env_var(mock_contract_class, expect, monkeypatch):
    # more about monkeypatch
    # https://docs.pytest.org/en/6.2.x/monkeypatch.html
    monkeypatch.setenv("CONTRACT_CLASS", mock_contract_class)
    assert use_env_var() == expect


"""
Exception
Let’s test the same use_env_var example, which was just used to demo for Environment Variable, but focusing on the exception scenario.

Here, we use pytest.raises as a context manager to capture the exception of the given type ValueError. Here, we could: 

specify the particular type of the Exception, e.g. ZeroDivisionError, KeyError.
specify the value message meets certain format following regular expression.
"""


def test_exception(monkeypatch):
    monkeypatch.setenv("CONTRACT_CLASS", "something not existed")
    with pytest.raises(
        ValueError, match=r"contract class something not existed not found"
    ):
        use_env_var()
