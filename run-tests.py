import pytest

#lista de archivos de prueba
test_files = [
    "test/test-login.py", "test/test-navigate.py",
]

pytest_args = test_files + [" --html=report.html","-v"]

pytest.main(pytest_args)
