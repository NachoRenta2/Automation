import pytest

#lista de archivos de prueba
test_files = [
    "tests/test-login.py", "tests/test-navigate.py"

    pytest_args = test_files =
    [" --html-report.html","-v"]

    pytest.main(pytest_args)
]